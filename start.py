import telebot
import random
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Топ 10 игр")
    item2 = types.KeyboardButton("Поиск игры по названию")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "дарова пользуйся клавой".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Топ 10 игр':
           bot.send_message(message.chat.id, 'Топ 10 игр: ')
           #todo
        elif message.text == 'Поиск игры по названию':
           bot.send_message(message.chat.id, 'Введите название')
           #todo
        else:
            bot.send_message(message.chat.id, 'пользуйся клавиатурой от телеграма дурак')


bot.polling(none_stop=True)
