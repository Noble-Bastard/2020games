import sqlite3
class Setter:

   def setGameInfo(self, game):
      database = sqlite3.connect('games.db', isolation_level=None)
      database.cursor().execute(
          "INSERT INTO games VALUES (NULL, ?, ?, ?, ?, ?)", (game['name'], game['link'], game['imageLink'], game['rating'], game['metacritic']))
      database.close()
