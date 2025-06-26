import os
import telebot

# Prende il token dalla variabile d'ambiente
TOKEN = os.environ.get("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello world 👋")

# Avvio in polling
bot.polling(none_stop=True)
