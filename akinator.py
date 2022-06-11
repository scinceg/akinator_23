from pip import main
import telebot
from telebot import types
import data


@data.bot.message_handler(commands=["start"])
def welcome(message):
    stiker = open(
        r"C:\Users\админ\Documents\Morrison\Back-end\Lessons\17_lesson\stiker.webp", "rb")
    data.bot.send_sticker(message.chat.id, stiker)

    welcome_str = "Привет, {0.first_name}, я <b>Акинатор</b>!".format(message.from_user,
                                                                      data.bot.get_me())

    simple_keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    color_key = types.KeyboardButton("Загадать цвет")

    simple_keyboard.add(color_key)

    data.bot.send_message(message.chat.id, welcome_str,
                          parse_mode="html", reply_markup=simple_keyboard)


@data.bot.message_handler(content_types=["text"])
def start(message):
    if message.chat.type == "private":
        if message.text == "Загадать цвет":
            game_text = "На данный момент я могу отгадывать один из этих цветов: {}, выбери цвет и нажми 'ПОЕХАЛИ!'.".format(
                data.color)

            go_keyboard = types.ReplyKeyboardMarkup( resize_keyboard=True, one_time_keyboard=True)
            go_key = types.KeyboardButton("ПОЕХАЛИ!")
            go_keyboard.add(go_key)
            data.bot.send_message(message.chat.id, game_text,
                                  parse_mode="html", reply_markup=go_keyboard)

        if message.text == "ПОЕХАЛИ!":
            for number_of_quenstions in range(len(data.question)):

                yesno_keyboard = types.ReplyKeyboardMarkup( resize_keyboard=True)
                yes_key = types.KeyboardButton("Да")
                no_key = types.KeyboardButton("Нет")
                yesno_keyboard.add(yes_key, no_key)

                if input(data.question[i][0]) == "1":
                    count += data.question[i][1]
                    print(count)


data.bot.polling(none_stop=True)
