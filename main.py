import telebot
from config import *
from solution import *

bot = telebot.TeleBot(token)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)  # main keyboard with 4 buttons
keyboard1.row('получить решение', 'показать схему', 'нашел ошибку')


@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Приветствую, я помогу тебе познать таинство схемы Горнера. Могу рассказать как она работает или решить уравнение', reply_markup = keyboard1)


@bot.message_handler(content_types = ['text'])
def send_text(message):  # if users message is a text
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет)')

    elif message.text.lower() == 'получить решение':
        bot.send_message(message.chat.id, 'Отлично, напиши "check",\
        а после твое уравнение вида "ax^n..+bx^2+cx+d=0"')

    elif message.text.lower() == 'нашел ошибку':
        bot.send_message(message.chat.id, 'Ну чтож, видимо я не идеален ..\
раз уж ты тут - сообщи об ошибке моему создателю, @JustNastyaa, спасибо')

    elif message.text.lower() == 'показать схему':
        bot.send_message(message.chat.id, theoryText)

    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

    elif 'check' in message.text.lower():
        ms = message.text.lower()
        bot.send_message(message.chat.id, solution(ms))
    else:
        bot.send_message(message.chat.id, 'Таких команд я не знаю')


bot.polling(none_stop=True)