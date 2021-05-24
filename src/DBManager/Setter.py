class Setter:
   def __init__(self, db):
      self.database = db

   def setGameInfo(self, game):
      self.database.cursor().execute("INSERT INTO games VALUES(?, ?, ?, ?);", game)
      self.database.commit()
