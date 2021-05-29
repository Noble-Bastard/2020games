import sqlite3

class Getter:

   def __init__(self):
      self.init = []


   def getGameInfo(self, game):
      database = sqlite3.connect('game.db', isolation_level=None)
      base = database.cursor().execute(
          "SELECT * FROM games WHERE name=(?)", (game,)).fetchall()
      database.close()
      return base


   def getTopTenGames(self):
      database = sqlite3.connect('game.db', isolation_level=None)
      cur = database.cursor()

      cur.execute("SELECT name FROM games;")
      results = cur.fetchmany(10) # сначала я загружаю первую десятку поэтмоу делаю через это, профит
      database.close()

      return results


   def getGameOnFirstChar(self, game, url):
      firstChar = game[0].upper()
      database = sqlite3.connect('game.db', isolation_level=None)
      cur = database.cursor()
      games = cur.execute("SELECT * FROM `games` WHERE name LIKE (?)", (firstChar + '%',)).fetchmany(10)
      names = []
      for item in games:
         names.append((item[1], url + item[2]))
      database.close()
      return names

