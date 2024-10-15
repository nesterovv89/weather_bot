from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn_1 = InlineKeyboardButton(text='Ввести город', callback_data='get')
btn_3 = InlineKeyboardButton(
    text='Узнать погоду для текущего местоположения', callback_data='current'
)
btn_2 = InlineKeyboardButton(text='Узнать в другом городе', callback_data='mm')

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[btn_1],
                     [btn_3],]
)

keyboard_2 = InlineKeyboardMarkup(
    inline_keyboard=[[btn_2],
                     [btn_3],]
)
