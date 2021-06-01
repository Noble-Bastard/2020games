from bs4 import BeautifulSoup
import requests
import sys


class Parser:

    def __init__(self, setterInstance):
        self.setter = setterInstance

    def parseInit(self, url, header):
        return requests.get(url, header)

    def getElements(self, response):
        soup = BeautifulSoup(response, 'lxml')
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

    def parser(self, startPages, pages, url, header={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/90.0.4430.212 Safari/537.36'}):
        for page in range(startPages, pages + 1):
            print(f' Парсинг страницы #{page}')
            response = self.parseInit(url + str(page), header)
            if response.status_code != 200:
                print(f" Произошла ошибка на странице #{page}")
                sys.exit()
            content = self.getElements(response.text)
            for game in content:
                self.setter.setGameInfo(game)
