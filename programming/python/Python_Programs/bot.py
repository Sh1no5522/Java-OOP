import os
import httpx
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TELEGRAM_BOT_TOKEN = "8561686209:AAEG9bCT_cCGTvwpSYLWso9Tfg2od88pEb8"
MISTRAL_API_KEY = "NmFPzKLCKBx7bQdNgCcyHsjbpZm9CacH"

# Запрос к Mistral AI
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


# Обработка сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.chat.send_action(action="typing")
    reply = await ask_mistral(user_text)
    await update.message.reply_text(reply)

# Запуск бота
async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Бот с Mistral AI запущен")
    await app.run_polling()

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())
