import os
import telebot

bot = telebot.TeleBot(os.environ.get("TELEGRAM_TOKEN"))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello world 👋")

bot.remove_webhook()
bot.polling(none_stop=True)
