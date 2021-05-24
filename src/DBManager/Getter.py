class Getter:
   def __init__(self, db):
      self.database = db

   def getGameInfo(self, game):
      return self.database.cursor().execute("SELECT * FROM games WHERE name='game'")

   def getTopTenGames(self):
      cur = self.database.cursor()

      cur.execute("SELECT * FROM games;")
      results = cur.fetchmany(10) # сначала я загружаю первую десятку поэтмоу делаю через это, профит
      self.database.commit()

      return results
