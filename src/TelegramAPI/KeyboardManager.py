class KeybordManager:

   def __init__(self, types):
      self.types = types

   def viewWelcome(self, text, text2, text3):
      markup = self.types.ReplyKeyboardMarkup(resize_keyboard=True)
      item1 = self.types.KeyboardButton(text)
      item2 = self.types.KeyboardButton(text2)
      item3 = self.types.KeyboardButton(text3)
      markup.add(item1, item2, item3)
      return markup

   def viewTopGames(self, text):
      markup = self.types.InlineKeyboardMarkup(row_width=2)
      item1 = self.types.InlineKeyboardButton(text[0], callback_data=text[0])
      item2 = self.types.InlineKeyboardButton(text[1], callback_data=text[1])
      item3 = self.types.InlineKeyboardButton(text[2], callback_data=text[2])
      item4 = self.types.InlineKeyboardButton(text[3], callback_data=text[3])
      item5 = self.types.InlineKeyboardButton(text[4], callback_data=text[4])
      item6 = self.types.InlineKeyboardButton(text[5], callback_data=text[5])
      item7 = self.types.InlineKeyboardButton(text[6], callback_data=text[6])
      item8 = self.types.InlineKeyboardButton(text[7], callback_data=text[7])
      item9 = self.types.InlineKeyboardButton(text[8], callback_data=text[8])
      item10 = self.types.InlineKeyboardButton(text[9], callback_data=text[9])

      markup.add(item1, item2, item3, item4,
                      item5, item6, item7, item8, item9, item10)
      return markup
