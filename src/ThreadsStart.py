from threading import Thread

class ThreadStart:

   def __init__(self, url):
      self.url = url

   def startParsing(self, parserClass, parserClass1, parserClass2, parserClass3, parserClass4, header):
      parserClass.parser(1, 20, self.url, header)
      thread = Thread(target=parserClass1.parser,
                      args=(241, 440, self.url, header,))
      thread1 = Thread(target=parserClass2.parser,
                       args=(441, 640, self.url, header,))
      thread2 = Thread(target=parserClass3.parser,
                       args=(641, 840, self.url, header,))
      thread3 = Thread(target=parserClass4.parser,
                       args=(841, 1040, self.url, header,))
      thread4 = Thread(target=parserClass4.parser,
                       args=(1041, 1348, self.url, header,))

      thread.start()
      thread1.start()
      thread2.start()
      thread3.start()
      thread4.start()
      parserClass.parser(21, 240, self.url, header)
      thread.join()
      thread1.join()
      thread2.join()
      thread3.join()
      thread4.join()
