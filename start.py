import telebot
import sqlite3
import config
from telebot import types
from src.TelegramAPI.KeybordManager import KeybordManager

# SQLite3
conn = sqlite3.connect('games.db')

def createDB(conn):
    conn.cursor().execute("""CREATE TABLE IF NOT EXISTS games(
        id INT PRIMARY KEY,
        name TEXT,
        rating INT,
        description TEXT);
    """)
    conn.commit()

createDB(conn)


#TelegramBot init
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

    board = KeybordManager(types.ReplyKeyboardMarkup(resize_keyboard=True), types)
    board.viewWelcome("Топ 10 игр", "Поиск по названию")

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
