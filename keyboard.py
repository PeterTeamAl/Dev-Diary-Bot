from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hello = "Hello. I got it, thanks!"

b_fsm_1 = KeyboardButton('FrontEnd')
b_fsm_2 = KeyboardButton('BackEnd')
b_fsm_3 = KeyboardButton('FullStack')
b_fsm_4 = KeyboardButton('Desctop')
b_fsm_5 = KeyboardButton('MobileDev')
b_fsm_6 = KeyboardButton('DataScience')
b_fsm_7 = KeyboardButton('GameDev')

b_fsm_8 = KeyboardButton("Junior")
b_fsm_9 = KeyboardButton("Middle")
b_fsm_10 = KeyboardButton("Senior")

markup_fsm_1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(b_fsm_1,b_fsm_2,b_fsm_3).row(b_fsm_4,b_fsm_5,b_fsm_6).add(b_fsm_7)

markup_fsm_2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(b_fsm_8,b_fsm_9,b_fsm_10)

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
greet_kb.add(button_hello)