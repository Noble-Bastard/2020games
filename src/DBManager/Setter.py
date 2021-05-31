import sqlite3

class Setter:


   def setGameInfo(self, game):
      games = True
      while games == True:
        try:
            database = sqlite3.connect('game.db', isolation_level=None)
            database.cursor().execute(
                "INSERT INTO games VALUES (NULL, ?, ?, ?, ?, ?, ?)", (game['name'], game['link'], game['imageLink'], game['rating'], game['metacritic'], game['category']))
            database.commit()
            database.close()
            break
        except Exception as e:
            print(e)
            return self.setGameInfo(game)
