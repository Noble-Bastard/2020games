class KeybordListener:

   def __init__(self, getterInstance, bot, manager, config):
      self.getTopGames = getterInstance
      self.bot = bot
      self.manager = manager
      self.config = config
      self.topGames = []


   def replykeyboardChecker(self, message):
      if message.chat.type == 'private':
          if message.text == self.config.MAINKEYBOARD['topten']:
             topGames = self.getTopGames.getNames()
             markup = self.manager.viewTopGames(topGames)
             self.bot.send_message(message.chat.id, 'Топ 10 игр: ', reply_markup=markup)
             self.topGames = topGames
           #todo
          elif message.text == self.config.MAINKEYBOARD['search']:
             msg = self.bot.reply_to(message, 'Введите название')
             self.bot.register_next_step_handler(msg, self.searchGame)
           #todo
          elif message.text == self.config.MAINKEYBOARD['help']:
             self.bot.send_message(message.chat.id, self.config.HELP)
           #todo
          else:
             self.bot.send_message(
                message.chat.id, 'пользуйся клавиатурой от телеграма дурак')


   def searchGame(self, message):
         info = self.getTopGames.getInfo(message.text, self.config)
         self.bot.send_message(message.chat.id, info, parse_mode="HTML")
         self.bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)


   def inlineKeyboardChecker(self, call):
      try:
         if call.message:
            if call.data in self.topGames:
              info = self.getTopGames.getInfo(call.data, self.config)
              self.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=info, parse_mode="HTML", reply_markup=None)

              self.bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Success!")
      except Exception as e:
        print(repr(e))
