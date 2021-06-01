class GetGames:

    def __init__(self, getter, parser):
        self.getter = getter
        self.parser = parser

    def getNames(self):
        names = []
        for item in self.getter.getTopTenGames():
            names.append(item[0])

        return names

    def getInfo(self, game, config):
        gameName = self.getter.getGameInfo(game)
        gamesList = f' '
        if gameName == []:
            games = self.getter.getGameOnFirstChar(game, config.SITE_URL)
            if games == []:
                return config.GETGAMES['uncorrectName']
            for game in games:
                gamesList = gamesList + f'Название: {game[0]} {game[1]}\n'
            return config.GETGAMES['alterGames'] + gamesList
        name = gameName[0][1]
        link = config.SITE_URL + str(gameName[0][2])
        rating = gameName[0][4]
        critic = gameName[0][5]
        category = gameName[0][6]
        imageLink = gameName[0][3]
        image = imageLink.replace("//", "")
        response = self.parser.parseInit(link)
        description = self.parser.getDescription(response)

        return f'<a href="{image}">&#8204;</a>' + f' Название: {name} {rating}⭐\n Категория: {category} \n \n Критика ' \
                                                  f'сайта: {critic}\n Описание: {description} '
