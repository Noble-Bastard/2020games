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
from time import time, sleep


# удаляем чтобы записи не перезаписывались при следующем включении
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'game.db')
os.remove(path)

os.environ['no_proxy'] = '127.0.0.1,localhost'#нужно удалить эту строчку если под линукс запускать

# SQLite3
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

start_time = time()
# start a parsing
cls = ThreadStart(config.FOR_PAGINATION_URL)
cls.startParsing(Parser(Setter()), Parser(
     Setter()), Parser(Setter()), Parser(Setter()))
    
print("--- %s seconds ---" % (time() - start_time))
print("Парсинг закончился, надеюсь успешно")

#TelegramBot init
bot = telebot.TeleBot(config.TOKEN)

board = KeybordManager(types)
boardText = config.MAINKEYBOARD
@bot.message_handler(commands=['start'])
def welcome(message):
    welcomeMarkup = board.viewWelcome(boardText['topten'], boardText["search"], boardText['help'])

    bot.send_message(message.chat.id, "дарова пользуйся клавой".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=welcomeMarkup)


listener = KeybordListener(GetGames(Getter(), Parser(Setter())), bot, board, config)

@bot.message_handler(content_types=['text'])
def replykeyboardResponse(message):
    listener.replykeyboardChecker(message)


@bot.callback_query_handler(func=lambda call: True)
def inlineKeyboardResponse(call):
    listener.inlineKeyboardChecker(call)


bot.polling(none_stop=True)