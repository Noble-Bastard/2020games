import telebot
import sqlite3
import config
import os

from telebot import types
from src.TelegramAPI.KeyboardManager import KeybordManager
from src.TelegramAPI.KeyboardListener import KeybordListener
from src.ThreadsStart import ThreadStart
from src.Parser import Parser
from src.DBManager.Setter import Setter
from src.DBManager.Getter import Getter
from src.GamesManager.GetGames import GetGames
from time import time

conn = sqlite3.connect('game.db', isolation_level=None)


def createDB(conn):
    conn.cursor().execute("""CREATE TABLE IF NOT EXISTS games(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        link TEXT,
        imageLink TEXT,
        rating TEXT,
        metacritic TEXT,
        category TEXT);
    """)
    conn.commit()


createDB(conn)
conn.close()

if config.PARSING == 0:
    start_time = time()
    cls = ThreadStart(config.FOR_PAGINATION_URL)
    cls.startParsing(Parser(Setter()), Parser(
        Setter()), Parser(Setter()), Parser(Setter()), Parser(Setter()), config.USER_AGENT)

    print("--- Парсинг завершен за %s секунд ---" % (time() - start_time))

bot = telebot.TeleBot(config.TOKEN)

board = KeybordManager(types)
boardText = config.MAINKEYBOARD


@bot.message_handler(commands=['start'])
def welcome(message):
    welcomeMarkup = board.viewWelcome(boardText['top-ten'], boardText["search"])

    bot.send_message(message.chat.id,
                     "В поисках игр 2020 года? Тогда тебе именно сюда! \n \n ? - Используй клавиатуру для быстрого "
                     "ввода" . format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=welcomeMarkup)


listener = KeybordListener(GetGames(Getter(), Parser(Setter())), bot, board, config)


@bot.message_handler(content_types=['text'])
def replykeyboardResponse(message):
    listener.replykeyboardChecker(message)


@bot.callback_query_handler(func=lambda call: True)
def inlineKeyboardResponse(call):
    listener.inlineKeyboardChecker(call)


bot.polling(none_stop=True)
