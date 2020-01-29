import telebot
from config  import (TOKEN, States)
from dbsettings  import (set_data_db, get_state, get_info)
import re
from telebot.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton)


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start_bot(message):
    state = get_state(message.chat.id)
    if state == States.FULL_NAME.value:
        bot.send_message(message.chat.id, "Знакомые люди, ответь пожалуйста - как тебя зовут?")
    elif state == States.NUMBER_PHONE.value:
        bot.send_message(message.chat.id, "Воу воу, помнишь спрашивал на счет номера телефона? напиши плиз..")
    elif state == States.MAIL.value:
        bot.send_message(message.chat.id, "Ну наконец то, как на счет email? скинь пожалуйста")
    elif state == States.ADDRESS.value:
        bot.send_message(message.chat.id, "Какой у тебя домашний адрес? напомни пожалуйста")
    elif state == States.WISHES.value:
        bot.send_message(message.chat.id, "Ну давай, не ломайсь, какие у тебя пожелания??")
    elif state == States.STOP.value:
        bot.send_message(message.chat.id, "Хочешь покажу что я о тебе знаю???")
    else:
        bot.send_message(message.chat.id, 'Привествую! Как к тебе обращаться?')
        set_data_db(message.chat.id, 'STATE_DIALOG', States.FULL_NAME.value)


# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=["reset"])
def reset_bot(message):
    bot.send_message(message.chat.id, "Ладно, давай по новой - как тебя зовут??")
    set_data_db(message.chat.id, 'STATE_DIALOG', States.FULL_NAME.value)


@bot.message_handler(func=lambda message: get_state(message.chat.id) == States.FULL_NAME.value)
def user_enter_name(message):
    set_data_db(message.chat.id, States.FULL_NAME.name, message.text)
    print(message.chat.id, States.FULL_NAME.name, message.text)
    bot.send_message(message.chat.id, "Просто МЕГО (: подскажи какой у тебя номер телефона?")
    set_data_db(message.chat.id, 'STATE_DIALOG', States.NUMBER_PHONE.value)


@bot.message_handler(func=lambda message: get_state(message.chat.id) == States.NUMBER_PHONE.value)
def user_enter_phone(message):
    if not (re.fullmatch('^\+?\d{1,3}?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d$', re.sub(r'[^0-9]', '', message.text))):
        bot.send_message(message.chat.id, "Не вредничай, введи корректный номер телефона..")
        return
    else:
        set_data_db(message.chat.id, States.NUMBER_PHONE.name, re.sub(r'[^0-9]', '', message.text))
        bot.send_message(message.chat.id, "Отлично, еще бы хотелось узнать твой Email")
        set_data_db(message.chat.id, 'STATE_DIALOG', States.MAIL.value)


@bot.message_handler(func=lambda message: get_state(message.chat.id) == States.MAIL.value)
def user_enter_mail(message):
    if not (re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', message.text)):
    # if not (re.match("^(?!\.)(""([^""\r\\]|\\[""\r\\])*""|([-a-z0-9!#$%&'*+/=?^_`{|}~]|(?<!\.)\.)*)(?<!\.)@[a-z0-9][\w\.-]*[a-z0-9]\.[a-z][a-z\.]*[a-z]$", message.text)):
        bot.send_message(message.chat.id,
                         "Давай попробуем еще раз, ты же хочешь получить интересные предложения на email?...>")
        return
    else:
        set_data_db(message.chat.id, States.MAIL.name, message.text)
        bot.send_message(message.chat.id,
                         "Мы почти окончили, подскажи, если я захочу тебе что то отправить, какой домашний адрес у тебя?")
        set_data_db(message.chat.id, 'STATE_DIALOG', States.ADDRESS.value)

@bot.message_handler(func=lambda message: get_state(message.chat.id) == States.ADDRESS.value)
def user_enter_mail(message):
    if not len(str(message.text).strip())>10:
        bot.send_message(message.chat.id, "Не теряй моё доверие, не обманывай меня - введи пожалуйста реальный адрес.")
        return
    else:
        set_data_db(message.chat.id, States.ADDRESS.name, message.text)
        bot.send_message(message.chat.id,"Спасибо, я стараюсь улучшить твою жизнь, оставь пожалуйста какие то пожелания")
        set_data_db(message.chat.id, 'STATE_DIALOG', States.WISHES.value)

@bot.message_handler(func=lambda message: get_state(message.chat.id) == States.WISHES.value)
def user_enter_mail(message):
    if not  len(str(message.text).strip())> 5: #len(set(message.text.split()))
        bot.send_message(message.chat.id, "Это последний шаг, неужели ты ничего не хочешь??\n Напиши свое пожелание и возможно я его выполню ;)")
        return
    else:
        set_data_db(message.chat.id, States.WISHES.name, message.text)
        bot.send_message(message.chat.id,
                         "Спасибо, я собрал о тебе всю интересующую информацию для спецслужб, наряд уже выехал.")
        set_data_db(message.chat.id, 'STATE_DIALOG', States.STOP.value)

@bot.message_handler(func=lambda message: get_state(message.chat.id) == States.STOP.value)
def get_data(message):
    txt = [', '.join(i) for i in get_info(message.chat.id)]
    bot.send_message(message.chat.id, txt)
    bot.send_message(message.chat.id, "Бай БАй")


if __name__ == '__main__':
    bot.polling()