from bs4 import BeautifulSoup
import requests
import sys
import sqlite3
from multiprocessing.dummy import Pool as ThreadPool
from time import time, sleep

class Parser:

   def __init__(self, setterInstance = None):
      self.setter = setterInstance

   def my_mega_function(self, url):
      request = requests.get(url, headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-language': 'en-US,en;q=0.8', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})
      print(request)
      if request.status_code == 503:
         return self.my_mega_function(url)
      soup = BeautifulSoup(request.text, 'lxml')
      return soup



   # user-agent стоит дефолтным мой, если что изменишь
   def parseInit(self, url, header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}):
      pool = ThreadPool(8)
      results = pool.map(self.my_mega_function, url)
      pool.close()
      pool.join()
      # pool = ThreadPool()
      # results = pool.map(requests.get, url)
      # print(results)
      return results


   def getElements(self, soup):
      items = soup.select('div.game-card')
      elements = []

      for item in items:
         elements.append(
            {
             'name': item.select_one('a.name').text,
             'link': item.select_one('a.name').get('href'),
             'imageLink': item.select_one('img.image').get('src'),
             'rating': item.select_one('div.users').select_one('span.value').text,
             'metacritic': item.select_one('div.metacritic').select_one('span.value').text,
             'category': ' '.join(item.select_one('div.tags').text.split())

            }
         )
      return elements


   def getDescription(self, response):
      soup = BeautifulSoup(response.content, 'lxml')
      desc = 'без описания'
      if soup.select_one('div.description') != None:
         return soup.select_one('div.description').text

      return desc
  

   def parser(self, startPages, pages, url='https://www.igromania.ru/games/all/all/2020/all/all/0/'):
      responseChecker = []
      for page in range(startPages, pages+1):
         print(f'Идет парсинг страницы {page}')
         # response = self.parseInit(url + str(page), {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'})
         # if response.status_code != 200:
         #    print(f"сайт не дал нужного ответа, скорее всего неправильный url или сайт лежит. Страница - {page}")
         #    sys.exit()
        # print(url + str(page))
         responseChecker.append(url + str(page))
      print(responseChecker)
      response = self.parseInit(responseChecker)
      print('123124124')
      start_time = time()
     # print(response)
      database = sqlite3.connect('game.db', isolation_level=None)
      for content in response:
         # print(self.getElements(content))
         self.setter.setGameInfo(self.getElements(content), database)
    #  print(elements)
      database.close()
      print("--- %s seconds ---" % (time() - start_time))

