import telebot
from telebot import types

from settings import TG_TOKEN, USER_ID, SHEET_URL
from google_sheets import get_total_revenue, add_row
from utils import create_button

bot = telebot.TeleBot(TG_TOKEN, parse_mode=None)

BTN_DOC = create_button('doc', '📝 Показать документ')
BTN_REV = create_button('rev', '💲 Общая выручка')
BTN_NEW_ITEM = create_button('new_item', '✅ Добавить продажу')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # img = open('hello.png', 'rb')  # TODO
    # bot.send_sticker(message.chat.id, img)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(BTN_DOC['title'])
    btn2 = types.KeyboardButton(BTN_REV['title'])
    btn3 = types.KeyboardButton(BTN_NEW_ITEM['title'])
    markup.add(btn1, btn2, btn3)

    bot.reply_to(message, 'Привет! Это твой личный помощник. Чего изволите?', reply_markup=markup)


@bot.message_handler(content_types='text')
def send_text(message):
    if message.text == BTN_DOC['title']:
        bot.send_message(message.chat.id, f'<a href="{SHEET_URL}">Отчет по продажам</a>', parse_mode='html')
    elif message.text == BTN_REV['title']:
        bot.send_message(message.chat.id, f'Общая выручка = <b>{get_total_revenue()} у.е. </b>',
                         parse_mode='html')
    elif message.text == BTN_NEW_ITEM['title']:
        new_item = [message.from_user.first_name]
        msg = bot.send_message(message.chat.id, 'Введите объект')
        bot.register_next_step_handler(msg, add_title, new_item=new_item)


@bot.message_handler(content_types='text')
def add_new_item(message):
    if message.text == BTN_NEW_ITEM['title']:
        new_item = [message.from_user.first_name]
        msg = bot.send_message(message.chat.id, 'Введите объект')
        bot.register_next_step_handler(msg, add_title, new_item=new_item)


def add_title(message, **kwargs):
    new_item = kwargs.get('new_item', [])
    new_item.append(message.text)
    msg = bot.send_message(message.chat.id, 'Введите сумму выручки')
    bot.register_next_step_handler(msg, add_revenue, new_item=new_item)


def add_revenue(message, **kwargs):
    new_item = kwargs.get('new_item', [])
    new_item.append(message.text)
    add_row(new_item)

    bot.send_message(message.chat.id, 'Спасибо 👍. Я добавил в отчет новую продажу.')