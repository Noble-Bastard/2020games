from threading import Thread
from DBManager.Setter import Setter
from time import time, sleep
import sqlite3
from Parser import Parser
import os
from DBManager.Setter import Setter

class ThreadsStart:

   def __init__(self, url):
      self.url = url


   def startParsing(self, parserClass, parserClass1, parserClass2, parserClass3):
      parserClass.parser(1, 10, self.url)
    #   thread = Thread(target=parserClass.parser,
    #                   args=(1, 10, self.url,))
    #   thread1 = Thread(target=parserClass1.parser,
    #                    args=(81, 120, self.url,))
    #   thread2 = Thread(target=parserClass2.parser,
    #                    args=(121, 160, self.url,))
    #   thread3 = Thread(target=parserClass3.parser,
    #                    args=(161, 200, self.url,))
# 
    #   thread.start()
    # #   thread1.start()
    # #   thread2.start()
    # #   thread3.start()
    # #   parserClass.parser(11, 40, self.url)
    #   thread.join()
    #   thread1.join()
    #   thread2.join()
    #   thread3.join()
#     

os.environ['no_proxy'] = '127.0.0.1,localhost'
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
cls = ThreadsStart('https://www.igromania.ru/games/all/all/2020/all/all/0/')
cls.startParsing(Parser(Setter()), Parser(Setter()),
                 Parser(Setter()), Parser(Setter()))
print("--- %s seconds ---" % (time() - start_time))

