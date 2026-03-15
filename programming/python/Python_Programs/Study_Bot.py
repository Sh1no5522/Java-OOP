import os
import httpx
import asyncio
import mysql.connector
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# --- CONFIG ---
TELEGRAM_BOT_TOKEN = "8561686209:AAEG9bCT_cCGTvwpSYLWso9Tfg2od88pEb8"
MISTRAL_API_KEY = "NmFPzKLCKBx7bQdNgCcyHsjbpZm9CacH"

# --- DB CONNECTION ---
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # add password if you have one
    database="studybot_db"
)
cursor = db.cursor()

# --- MISTRAL AI REQUEST ---
async def ask_mistral(prompt: str) -> str:
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "mistral-small",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(url, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
    except httpx.ReadTimeout:
        return "⏳ Mistral API timed out. Please try again later."
    except httpx.HTTPStatusError as e:
        return f"❌ API error: {e.response.status_code}"
    except Exception as e:
        return f"⚠️ Unexpected error: {str(e)}"

# --- REGISTRATION / AUTHORIZATION ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    username = user.username
    first_name = user.first_name

    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    existing_user = cursor.fetchone()

    if existing_user:
        await update.message.reply_text(
            f"👋 Welcome back, {first_name}! You’re already registered as a {existing_user[3]}."
        )
    else:
        cursor.execute(
            "INSERT INTO users (user_id, username, first_name) VALUES (%s, %s, %s)",
            (user_id, username, first_name)
        )
        db.commit()
        await update.message.reply_text(
            f"✅ Hello {first_name}! You’ve been registered successfully in Study Bot. "
            "You can now send me text or YouTube links to summarize!"
        )

# --- MAIN CHAT HANDLER ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id

    # Check if user registered
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    registered = cursor.fetchone()
    if not registered:
        await update.message.reply_text("⚠️ Please use /start to register before using the bot.")
        return

    # Process user message
    user_text = update.message.text
    await update.message.chat.send_action(action="typing")
    reply = await ask_mistral(user_text)
    await update.message.reply_text(reply)

# --- /profile command ---
async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    cursor.execute("SELECT username, first_name, role, join_date FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()

    if user:
        await update.message.reply_text(
            f"👤 *Your Profile:*\n"
            f"Username: @{user[0]}\n"
            f"Name: {user[1]}\n"
            f"Role: {user[2]}\n"
            f"Joined: {user[3]}",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text("You are not registered yet! Use /start first.")

# --- RUN BOT ---
async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("profile", profile))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Study Bot with registration is running...")
    await app.run_polling()

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())
