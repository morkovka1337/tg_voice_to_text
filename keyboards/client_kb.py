from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = KeyboardButton('НАЧАТЬ')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True) \
    .add(start)
