import asyncio
import httpx
import mysql.connector
import re

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
    filters
)

from youtube_transcript_api import YouTubeTranscriptApi


TELEGRAM_BOT_TOKEN = "8561686209:AAEG9bCT_cCGTvwpSYLWso9Tfg2od88pEb8"
MISTRAL_API_KEY = "NmFPzKLCKBx7bQdNgCcyHsjbpZm9CacH"


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studybot_db",
    autocommit=True
)
cursor = db.cursor(buffered=True)


video_waiting_users = set()

def is_admin(user_id):
    cursor.execute("SELECT role FROM users WHERE user_id = %s", (user_id,))
    r = cursor.fetchone()
    return r and r[0] == "admin"


def extract_video_id(url):
    patterns = [
        r"v=([^&]+)",
        r"youtu\.be/([^?]+)"
    ]
    for p in patterns:
        match = re.search(p, url)
        if match:
            return match.group(1)
    return None


from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, \
    CouldNotRetrieveTranscript


async def get_youtube_transcript(url):
    api_key = "sd_70b7243c440132925a1cae037298df59"
    endpoint = f"https://api.supadata.ai/v1/transcript?url={url}"
    headers = {"x-api-key": api_key}

    async with httpx.AsyncClient() as client:
        response = await client.get(endpoint, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return " ".join([item['text'] for item in data.get('content', [])])
    return None


async def ask_mistral(prompt: str) -> str:
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "mistral-small",
        "messages": [
            {"role": "system", "content": "You are a concise assistant. Summarize into 5 bullet points max."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 300
    }

    try:
        async with httpx.AsyncClient(timeout=45.0) as client:
            response = await client.post(url, headers=headers, json=body)
            return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ AI Timeout. The video might be too long. Error: {e}"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user.id,))
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO users (user_id, username, first_name) VALUES (%s, %s, %s)",
            (user.id, user.username, user.first_name)
        )
    await update.message.reply_text("✅ You are registered! Send text or use /video.")


async def video_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video_waiting_users.add(update.effective_user.id)
    await update.message.reply_text("📹 Please send a YouTube link to summarize.")



async def admin_dashboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("⛔ Access denied.")
        return

    keyboard = [
        [InlineKeyboardButton("👥 View Users", callback_data="admin_users")],
        [InlineKeyboardButton("📊 Bot Stats", callback_data="admin_stats")]
    ]
    await update.message.reply_text(
        "🛠️ <b>Admin Dashboard</b>",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )


async def admin_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if not is_admin(update.effective_user.id):
        return

    if query.data == "admin_users":
        cursor.execute("SELECT user_id, first_name, username FROM users")
        users = cursor.fetchall()

        keyboard = [
            [InlineKeyboardButton(f"{u[1]} (@{u[2]})", callback_data=f"user_{u[0]}")]
            for u in users
        ]
        keyboard.append([InlineKeyboardButton("⬅️ Back", callback_data="admin_back")])

        await query.edit_message_text(
            "👤 <b>Select user:</b>",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="HTML"
        )

    elif query.data.startswith("user_"):
        uid = query.data.split("_")[1]
        cursor.execute(
            "SELECT user_message, bot_response FROM chat_history WHERE user_id=%s ORDER BY created_at DESC LIMIT 5",
            (uid,)
        )
        rows = cursor.fetchall()

        text = f"📝 <b>Last messages for user {uid}</b>\n\n"
        for r in rows:
            text += f"❓ {r[0][:60]}\n🤖 {r[1][:60]}\n\n"

        await query.edit_message_text(
            text,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅️ Back", callback_data="admin_users")]]
            ),
            parse_mode="HTML"
        )

    elif query.data == "admin_stats":
        cursor.execute("SELECT COUNT(*) FROM users")
        users = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM chat_history")
        msgs = cursor.fetchone()[0]

        await query.edit_message_text(
            f"📊 <b>Stats</b>\nUsers: {users}\nMessages: {msgs}",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅️ Back", callback_data="admin_back")]]
            ),
            parse_mode="HTML"
        )

    elif query.data == "admin_back":
        await admin_dashboard(update, context)



processed_messages = set()


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message_id = update.message.message_id
    text = update.message.text

    if message_id in processed_messages:
        return
    processed_messages.add(message_id)

    try:
        if user_id in video_waiting_users:
            video_waiting_users.remove(user_id)

            status_msg = await update.message.reply_text("⏳ Processing video...")

            transcript = await get_youtube_transcript(text)

            if not transcript:
                await status_msg.edit_text("❌ No subtitles available.")
                return

            await status_msg.edit_text("🤖 AI is summarizing...")
            reply = await ask_mistral(f"Summarize this:\n{transcript[:5000]}")

            await status_msg.edit_text(reply)

        else:
            reply = await ask_mistral(text)
            await update.message.reply_text(reply)

        cursor.execute(
            "INSERT INTO chat_history (user_id, user_message, bot_response) VALUES (%s, %s, %s)",
            (user_id, text[:255], reply[:1000])
        )
        db.commit()

    finally:
        if len(processed_messages) > 100:
            processed_messages.clear()


def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("video", video_command))
    app.add_handler(CommandHandler("admin", admin_dashboard))
    app.add_handler(CallbackQueryHandler(admin_buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Study Bot is running...")
    app.run_polling()



if __name__ == "__main__":
    main()

