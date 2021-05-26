from threading import Thread
from Setter import Setter
from Parser import Parser
import sqlite3
from time import time
import os

class ThreadStart:

   def __init__(self, url):
      self.url = url


   def startParsing(self, parserClass):
      threadX = Thread(target=parserClass.parser,
                       args=(1, 66, self.url,))
      thread = Thread(target=parserClass.parser,
                      args=(67, 132, self.url,))
      thread1 = Thread(target=parserClass.parser,
                       args=(133, 200, self.url,))
    #   thread2 = Thread(target=parserClass.parser,
    #                    args=(121, 160, self.url,))
    #   thread3 = Thread(target=parserClass.parser,
    #                    args=(161, 200, self.url,))
      threadX.start()
      thread.start()
      thread1.start()
    #   thread2.start()
    #   thread3.start()
      threadX.join()
      thread.join()
      thread1.join()
    #   thread2.join()
    #   thread3.join()
    #  parserClass.parser(1, 40, self.url)



# TESTS
os.environ['no_proxy'] = '127.0.0.1,localhost'

conn = sqlite3.connect('games.db', isolation_level=None)
def createDB(conn):
    conn.cursor().execute("""CREATE TABLE IF NOT EXISTS games(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        link TEXT,
        imageLink TEXT,
        rating TEXT,
        metacritic TEXT);
    """)
    conn.commit()

createDB(conn)

start_time = time()

cls = ThreadStart('https://www.igromania.ru/games/all/all/2020/')
cls.startParsing(Parser(Setter()))

print("--- %s seconds ---" % (time() - start_time))



