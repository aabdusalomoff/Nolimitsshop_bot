from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
    InlineKeyboardMarkup, InlineKeyboardButton)



START_BUTTONS = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Ro‘yxatdan o‘tish"), KeyboardButton(text="📋 Menu")],
        [KeyboardButton(text="📦 Buyurtmalar"), KeyboardButton(text="📞 Aloqa")]
    ],
    resize_keyboard=True
)


REGISTER_SUCCESS_BUTTONS = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📋 Menu")],
        [KeyboardButton(text="📦 Buyurtmalar")], 
        [KeyboardButton(text="📞 Aloqa")]
    ],
    resize_keyboard=True
)


PHONE_BUTTON = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Phone", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

LOCATION_BUTTON = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Location", request_location=True)]
    ],
    resize_keyboard=True
)

GENDER_BUTTON = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👨 Erkak", callback_data="gender_erkak"),
            InlineKeyboardButton(text="👩 Ayol", callback_data="gender_ayol")
        ]
    ]
)