# Подключаем модуль случайных чисел
import random

# Подключаем модуль для Телеграма
# PyTelegramBotAPI
import telebot
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Указываем токен с подключением Yaml файла
import yaml

with open(r'config.yaml', 'r') as f:
    config = yaml.safe_load(f)
    token = config['access_token']

bot = telebot.TeleBot(token)

# считывание данных из файлов
with open("shtirlits.txt", "r", encoding="utf-8") as f:
    for line in f:
        shtirlits = line.split('*')
with open("rzhevskiy.txt", "r", encoding="utf-8") as f:
    for line in f:
        rzhevskiy = line.split('*')
with open("vasiliy.txt", "r", encoding="utf-8") as f:
    for line in f:
        vasiliy = line.split('*')
with open("chukcha.txt", "r", encoding="utf-8") as f:
    for line in f:
        chukcha = line.split('*')
with open("vovochka.txt", "r", encoding="utf-8") as f:
    for line in f:
        vovochka = line.split('*')
with open("animals.txt", "r", encoding="utf-8") as f:
    for line in f:
        animals = line.split('*')
with open("barin.txt", "r", encoding="utf-8") as f:
    for line in f:
        barin = line.split('*')

# Метод, который получает сообщения и обрабатывает их

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text.capitalize() == "Привет" or message.text.capitalize() == "Hi":

        # Пишем приветствие

        # bot.send_message(message.from_user.id, "Привет, слушай тост!")

        # Готовим кнопки

        keyboard = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик для каждого вида тоста

        key_shtirlits = types.InlineKeyboardButton(text='Штирлиц', callback_data='shtirlits')

        # И добавляем кнопку на экран

        keyboard.add(key_shtirlits)

        key_rzhevskiy = types.InlineKeyboardButton(text='Поручик Ржевский', callback_data='rzhevskiy')

        keyboard.add(key_rzhevskiy)

        key_vasiliy = types.InlineKeyboardButton(text='Чапаев', callback_data='vasiliy')

        keyboard.add(key_vasiliy)

        key_chukcha = types.InlineKeyboardButton(text='Чукча', callback_data='chukcha')

        keyboard.add(key_chukcha)

        key_vovochka = types.InlineKeyboardButton(text='Вовочка', callback_data='vovochka')

        keyboard.add(key_vovochka)

        key_animals = types.InlineKeyboardButton(text='Животный мир', callback_data='animals')

        keyboard.add(key_animals)

        key_barin = types.InlineKeyboardButton(text='Барин и слуга', callback_data='barin')

        keyboard.add(key_barin)

        # Показываем все кнопки сразу и пишем сообщение о выборе

        bot.send_message(message.from_user.id, text='Привет {}, выбери анекдот'.format(message.from_user.first_name),
                         reply_markup=keyboard)

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши Привет или Hi")

    else:

        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из кнопок — выводим тосты
    msg = ''
    if call.data == "shtirlits":
        msg = random.choice(shtirlits)
    elif call.data == "rzhevskiy":
        msg = random.choice(rzhevskiy)
    elif call.data == "vasiliy":
        msg = random.choice(vasiliy)
    elif call.data == "chukcha":
        msg = random.choice(chukcha)
    elif call.data == "vovochka":
        msg = random.choice(vovochka)
    elif call.data == "animals":
        msg = random.choice(animals)
    elif call.data == "barin":
        msg = random.choice(barin)

    # bot.delete_message(call.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, msg)

    # bot.delete_message(call.message.chat.id, call.message.message_id)
    # print(call.message.chat.id,call.message.message_id,msg)
    # Запускаем постоянный опрос бота в Телеграме


bot.polling(none_stop=True, interval=0)
