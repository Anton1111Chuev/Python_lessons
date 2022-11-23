import os
import telebot
from handler_control import Handler_control

def get_token():
    pass

token = get_token()

def init_bot():
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, "Hello! \n "
                                          "Поиск по имени или телефону - любой текст\n"
                                          "Получить файл с данными - команда /getfile")

    @bot.message_handler(commands=['getfile'])
    def getfile(message):
        handler_control = Handler_control()   # если инициализировать ранее т.к. создается соединение с БД и  оно остается для оптимизации на весь срок жизни объекта то Алхимия на потоки ругается т.к. следующая команда запускается в отдельном потоке
        result = handler_control.save_json()
        bot.send_message(message.chat.id, result)
        if os.path.isfile("data.txt"):
            with open("data.txt", "rb") as file:
                f = file.read()
            bot.send_document(message.chat.id, f)

    @bot.message_handler()
    def command_help(message):
        handler_control = Handler_control()
        result = handler_control.get_data(message.text)
        bot.send_message(message.chat.id, result)

    bot.polling(none_stop=True, interval=0)
