import telebot
from telebot.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton)
from keyboards import START_KB, NEWS_KB
from words import GREETINGS, NEWS_TEXT
from config import TOKEN
# GREETINGS = {
#     'привет' : 'Привет!',
#     'hi':'Hello',
# }
#
#
# TOKEN = '988581457:AAGTtV81u_YTzQwOf6qG6yvDRGmQNJw0-PQ'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_bot(message):
    #message.text - Текст сообщения
    #message.chat.id - Айди чата = айди юзера
    #message.from_user.id - Айди чата
    #message.message_id - Айди сообщения
    print(message)
    # bot.send_message(message.chat.id,'Hello,\n купи слона! ')
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(value) for value in START_KB.values()]
    kb.add(*buttons)
    bot.send_message(message.chat.id, 'Hello,\n купи слона! ', reply_markup=kb)


def check_greetings(message):
    return message.text.lower() in GREETINGS.keys()

# @bot.message_handler(func=lambda message: message.text.lower() in GREETINGS.keys())
@bot.message_handler(func=check_greetings)
def hello(message):
    bot.send_message(message.chat.id, GREETINGS[message.text.lower()])

@bot.message_handler(func=lambda message: message.text == START_KB['main'])
def main(message):
    bot.send_message(message.chat.id,
                     f'{GREETINGS["здравствуй"]} ты на главной странице!')

@bot.message_handler(func=lambda message: message.text == START_KB['news'])
def get_news(message):
    kb = InlineKeyboardMarkup(row_width=1)
    buttons = [InlineKeyboardButton(callback_data=str(key), text=value) for key, value in NEWS_KB.items()]
    kb.add(*buttons)
    bot.send_message(message.chat.id,f'Выберите новость!', reply_markup=kb)

@bot.callback_query_handler(func= lambda call: True)
def callback(call):
    print(call)
    bot.send_message(call.message.chat.id, NEWS_TEXT[call.data])

@bot.message_handler(content_types=['text'])
def reverse_message(message):
    text = message.text[::-1]
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text == 'Привет')
def hello(message):
    bot.send_message(message.chat.id, 'Приветос')

if __name__ == '__main__':
    bot.polling()