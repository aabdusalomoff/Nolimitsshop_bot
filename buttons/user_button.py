from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
    InlineKeyboardMarkup, InlineKeyboardButton)

GENDER_BUTTONS = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🧔 Erkaklar uchun", callback_data="menu_gender_male"),
            InlineKeyboardButton(text="👩 Ayollar uchun", callback_data="menu_gender_female"),
            InlineKeyboardButton(text="🧒 Bolalar uchun", callback_data="menu_gender_kids")
        ]
    ]
)