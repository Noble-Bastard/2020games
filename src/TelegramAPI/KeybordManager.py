class KeybordManager:

   def __init__(self, markup, types):
      self.markup = markup
      self.types = types

   def viewWelcome(self, text, text2):

      item1 = self.types.KeyboardButton(text)
      item2 = self.types.KeyboardButton(text2)
      self.markup.add(item1, item2)

   def viewTopGames(self, texts):
   
      item1 = self.types.KeyboardButton(text[0])
      item2 = self.types.KeyboardButton(text[1])
      item3 = self.types.KeyboardButton(text[2])
      item4 = self.types.KeyboardButton(text[3])
      item5 = self.types.KeyboardButton(text[4])
      item6 = self.types.KeyboardButton(text[5])
      item7 = self.types.KeyboardButton(text[6])
      item8 = self.types.KeyboardButton(text[7])
      item9 = self.types.KeyboardButton(text[9])
      item10 = self.types.KeyboardButton(text[10])

      self.markup.add(item1, item2, item3, item4,
                      item5, item6, item7, item8, item9, item10)
