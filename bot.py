# Подключаем модуль случайных чисел
import random

# Подключаем модуль для Телеграма
#PyTelegramBotAPI
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
# with open("housewife2.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         housewife = line.split('*')
# with open("health2.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         health = line.split('*')
# with open("man2.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         man = line.split('*')
# with open("birthday2.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         birthday = line.split('*')


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

        # key_housewife = types.InlineKeyboardButton(text='ЗА ХОЗЯЙКУ', callback_data='housewife')
        #
        # keyboard.add(key_housewife)
        #
        # key_housewife = types.InlineKeyboardButton(text='ЗА ЗДОРОВЬЕ', callback_data='housewife')
        #
        # keyboard.add(key_housewife)
        #
        # key_man = types.InlineKeyboardButton(text='ЗА МУЖЧИН', callback_data='man')
        #
        # keyboard.add(key_man)
        #
        # key_birthday = types.InlineKeyboardButton(text='ЗА ВИНОВНИКА ТОРЖЕСТВА', callback_data='birthday')
        #
        # keyboard.add(key_birthday)

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
    # elif call.data == "housewife":
    #     msg = random.choice(housewife)
    # elif call.data == "health":
    #     msg = random.choice(health)
    # elif call.data == "man":
    #     msg = random.choice(man)
    # elif call.data == "birthday":
    #     msg = random.choice(birthday)

    # bot.delete_message(call.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, msg)

    # bot.delete_message(call.message.chat.id, call.message.message_id)
    # print(call.message.chat.id,call.message.message_id,msg)
    # Запускаем постоянный опрос бота в Телеграме


bot.polling(none_stop=True, interval=0)
