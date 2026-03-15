import os
import openai
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Set your tokens
TELEGRAM_BOT_TOKEN = "7868459232:AAEjoMDWULzwmAPbATxh2bVuS2-SCbTFlBU"
OPENAI_API_KEY = "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"

# Configure OpenAI
openai.api_key = OPENAI_API_KEY

# Function to send message to ChatGPT
async def ask_chatgpt(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or "gpt-4" if you have access
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# Telegram message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.chat.send_action(action="typing")
    reply = await ask_chatgpt(user_message)
    await update.message.reply_text(reply)

# Main bot setup
async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot is running...")
    await app.run_polling()

# Run bot with asyncio
if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())
