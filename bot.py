import telebot
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    print("❌ Ошибка: отсутствует TELEGRAM_BOT_TOKEN")
    exit(1)

print("✅ Бот запускается...")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой бот. Чем могу помочь?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
