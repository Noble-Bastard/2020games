from bs4 import BeautifulSoup
import requests
import config


def parseInit(url, header):
   return requests.get(url, header)

def parse(response):
   soup =  BeautifulSoup(response.content, 'lxml')
   items = soup.select('div.game-card')
   elements = []

   for item in items:
      elements.append(
         {
             'name': item.select_one('a.name').text,
             'image': item.select_one('a.name').text

         }
      )
   return elements

response = parseInit(config.SITE_URL, {'User-Agent': config.USER_AGENT})

da = parse(response)
for item in da:
   print(item['name'])
