import asyncio
import httpx
import mysql.connector
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
    filters
)


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



def is_admin(user_id):
    db.commit()
    cursor.execute("SELECT role FROM users WHERE user_id = %s", (user_id,))
    r = cursor.fetchone()
    return r and r[0] == "admin"


async def ask_mistral(prompt: str) -> str:
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {MISTRAL_API_KEY}", "Content-Type": "application/json"}
    body = {"model": "mistral-small", "messages": [{"role": "user", "content": prompt}]}
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(url, headers=headers, json=body)
            return response.json()["choices"][0]["message"]["content"]
    except:
        return "⚠️ Error."



async def admin_dashboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("⛔ Access Denied.")
        return

    keyboard = [
        [InlineKeyboardButton("👥 View All Users", callback_data="admin_view_users")],
        [InlineKeyboardButton("📊 Bot Stats", callback_data="admin_view_stats")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🛠️ <b>Admin Dashboard</b>\nSelect a section:",
                                    reply_markup=reply_markup, parse_mode="HTML")


async def admin_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = update.effective_user.id
    await query.answer()

    if not is_admin(user_id):
        return

    if query.data == "admin_view_users":
        cursor.execute("SELECT user_id, first_name, username FROM users")
        users = cursor.fetchall()
        keyboard = []
        for u in users:
            keyboard.append([InlineKeyboardButton(f"{u[1]} (@{u[2]})", callback_data=f"user_hist_{u[0]}")])

        keyboard.append([InlineKeyboardButton("⬅️ Back", callback_data="admin_back")])
        await query.edit_message_text("👤 <b>Select a user to see their history:</b>",
                                      reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")

    elif query.data.startswith("user_hist_"):
        target_id = query.data.split("_")[2]
        cursor.execute(
            "SELECT user_message, bot_response FROM chat_history WHERE user_id = %s ORDER BY created_at DESC LIMIT 5",
            (target_id,))
        rows = cursor.fetchall()

        history_text = f"📝 <b>Last 5 messages for ID {target_id}:</b>\n\n"
        if not rows:
            history_text += "No history found."
        for r in rows:
            history_text += f"❓ {r[0][:50]}\n🤖 {r[1][:50]}\n\n"

        keyboard = [[InlineKeyboardButton("⬅️ Back to Users", callback_data="admin_view_users")]]
        await query.edit_message_text(history_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")

    elif query.data == "admin_view_stats":
        cursor.execute("SELECT COUNT(*) FROM users")
        u_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM chat_history")
        m_count = cursor.fetchone()[0]

        text = f"📊 <b>Stats</b>\nUsers: {u_count}\nMessages: {m_count}"
        keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data="admin_back")]]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")

    elif query.data == "admin_back":
        keyboard = [
            [InlineKeyboardButton("👥 View All Users", callback_data="admin_view_users")],
            [InlineKeyboardButton("📊 Bot Stats", callback_data="admin_view_stats")]
        ]
        await query.edit_message_text("🛠️ <b>Admin Dashboard</b>",
                                      reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user.id,))
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (user_id, username, first_name) VALUES (%s, %s, %s)",
                       (user.id, user.username, user.first_name))
    await update.message.reply_text("✅ Registered!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_text = update.message.text
    await update.message.chat.send_action("typing")
    reply = await ask_mistral(user_text)
    cursor.execute("INSERT INTO chat_history (user_id, user_message, bot_response) VALUES (%s, %s, %s)",
                   (user_id, user_text, reply))
    await update.message.reply_text(reply)



async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).job_queue(None).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin_dashboard))
    app.add_handler(CallbackQueryHandler(admin_button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Admin Bot is live...")
    await app.run_polling()


if __name__ == "__main__":
    import nest_asyncio

    nest_asyncio.apply()
    asyncio.run(main())