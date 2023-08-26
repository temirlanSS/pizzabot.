from telebot import TeleBot, types

def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('Меню')
    button2 = types.KeyboardButton ('Корзина')
    keyboard.add(button1, button2)
    return keyboard