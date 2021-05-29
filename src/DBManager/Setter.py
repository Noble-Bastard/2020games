import sqlite3

class Setter:

   def setGameInfo(self, games, database):
      for game in games:
        database.cursor().execute(
          "INSERT INTO games VALUES (NULL, ?, ?, ?, ?, ?, ?)", (game['name'], game['link'], game['imageLink'], game['rating'], game['metacritic'], game['category']))
      database.commit()
