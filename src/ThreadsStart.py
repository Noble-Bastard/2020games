from threading import Thread
# from Setter import Setter
# from Parser import Parser
# import sqlite3
# from time import time
# import os

class ThreadStart:

   def __init__(self, url):
      self.url = url


   def startParsing(self, parserClass, parserClass1, parserClass2, parserClass3):
      parserClass.parser(1, 10, self.url)
      thread = Thread(target=parserClass1.parser,
                      args=(50, 99, self.url,))
      thread1 = Thread(target=parserClass2.parser,
                       args=(100, 149, self.url,))
      thread2 = Thread(target=parserClass3.parser,
                       args=(150, 200, self.url,))

      thread.start()
      thread1.start()
      thread2.start()
      parserClass.parser(11, 49, self.url)
      thread.join()
      thread1.join()
      thread2.join()



