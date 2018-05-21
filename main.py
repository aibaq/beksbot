from constants import TOKEN
from messages import HELLO, CURRENT_WEATHER
from telebot import types
import messages
import database
# pytelegrambotapi
import telebot
import requests


bot = telebot.TeleBot(TOKEN)

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('Almaty')
itembtn2 = types.KeyboardButton('Astana')
itembtn3 = types.KeyboardButton('Krg')
itembtn4 = types.KeyboardButton('Pavlodar')
itembtn5 = types.KeyboardButton('Aktobe')
markup.row(itembtn1)
markup.row(itembtn2, itembtn3, itembtn4)
markup.row(itembtn5)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, messages.HELLO)
    msg = ''
    for i in database.get():
        msg += str(i)
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['weather'])
def get_weather(message):
    # bot.reply_to(message, CURRENT_WEATHER)
    # print(message)
    # bot.send_message(message.chat.id, CURRENT_WEATHER)
    my_message = str(message)
    database.insert({'msg': my_message})
    print('inserted')
    bot.send_message(message.chat.id, "Choose City:", reply_markup=markup)


@bot.message_handler(commands=['photo'])
def send_photo(message):
    photo = open('photos/liverpool.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()


if __name__ == '__main__':
    print('Starting BeksBot')
    bot.polling()
