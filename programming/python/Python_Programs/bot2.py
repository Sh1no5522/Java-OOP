import aiohttp
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# ВСТАВЬ СЮДА СВОЙ Telegram Bot Token и OpenRouter API Key
TELEGRAM_BOT_TOKEN = "7868459232:AAEjoMDWULzwmAPbATxh2bVuS2-SCbTFlBU"
OPENROUTER_API_KEY = "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"

# Основная функция для общения с Mistral через OpenRouter
async def ask_mistral(prompt: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://t.me/YourTelegramUsername",  # можно указать свой username
        "X-Title": "BolatBot"
    }
    body = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=body) as resp:
            if resp.status != 200:
                return f"Ошибка: {resp.status}"
            data = await resp.json()
            return data["choices"][0]["message"]["content"]

# Обработка входящих сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.chat.send_action(action="typing")
    reply = await ask_mistral(user_text)
    await update.message.reply_text(reply)

# Основной запуск бота
async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Бот запущен")
    await app.run_polling()

# Запуск
if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
