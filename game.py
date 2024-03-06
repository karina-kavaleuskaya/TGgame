import telebot
import random
from telebot import types

bot = telebot.TeleBot("****")

game = ["Камень", "Ножницы", "Бумага"]
@bot.message_handler(commands = ['start'])
def handle_start(message):

    keyboard = types.ReplyKeyboardMarkup(True)
    button_one  = types.KeyboardButton("Камень")
    button_two = types.KeyboardButton("Ножницы")
    button_three = types.KeyboardButton("Бумага")
    keyboard.add(button_one, button_two, button_three)

    bot.send_message(message.chat.id, "Hello!", reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_message(message):

    random_object = random.choice(game)
    if random_object == 'Камень' and message.text =='Ножницы':
        result ='Ты проиграл'
    elif random_object == 'Камень' and message.text =='Бумага':
        result ='Ты выиграл'
    elif random_object == 'Камень' and message.text =='Камень':
        result ='Ничья'
    elif random_object == 'Ножницы' and message.text =='Бумага':
        result ='Ты проиграл'
    elif random_object == 'Ножницы' and message.text =='Ножницы':
        result ='Ничья'
    elif random_object == 'Ножницы' and message.text =='Камень':
        result ='Ты выиграл'
    elif random_object == 'Бумага' and message.text == 'Камень':
        result = 'Ты проиграл'
    elif random_object == 'Бумага' and message.text == 'Бумага':
        result = 'Ничья'
    elif random_object == 'Бумага' and message.text == 'Ножницы':
        result = 'Ты выиграл'

    bot.send_message(message.chat.id, random_object)
    bot.reply_to(message, result)

bot.polling(non_stop = True)