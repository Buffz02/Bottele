import os
import telebot

TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello world 👋")

# 👇 Disattiva webhook se attivo
bot.remove_webhook()
bot.polling(none_stop=True)
