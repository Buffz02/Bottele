import os
import telebot

# Prende il token dalla variabile d'ambiente
TOKEN = os.environ.get("7561299513:AAHnXCVpON1Cv20v3QgP0DaxS5dCdhe6hfE")

bot = telebot.TeleBot(TOKEN)

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello world 👋")

# Avvio in polling
bot.polling(none_stop=True)
