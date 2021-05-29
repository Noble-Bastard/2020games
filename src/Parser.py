from bs4 import BeautifulSoup
import requests
import sqlite3
import sys

class Parser:

   def __init__(self, setterInstance):
      self.setter = setterInstance


   # user-agent стоит дефолтным мой, если что изменишь
   def parseInit(self, url, header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}):
      return requests.get(url, header)

   def getElements(self, response):
      soup =  BeautifulSoup(response, 'lxml')
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
  
   def parser(self, startPages, pages, url):
      for page in range(startPages, pages+1):
         print(f'Идет парсинг страницы {page}')
         response = self.parseInit(url + str(page), {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'})
         if response.status_code != 200:
            print(f"сайт не дал нужного ответа, скорее всего неправильный url или сайт лежит{page}")
            esys.exit()
         database = sqlite3.connect('game.db', isolation_level=None)
         self.setter.setGameInfo(self.getElements(response.text), database)
         database.close()


   
