from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
    InlineKeyboardMarkup, InlineKeyboardButton)

from database import get_category

ADMIN_REGISTER = ReplyKeyboardMarkup(
    keyboard=[
       [KeyboardButton(text="📝 Ro‘yxatdan o‘tish")]
    ],
    resize_keyboard=True
)

ADMIN_MENU = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text= '📊 Dashboard')],
        [KeyboardButton(text='🧾 Menu')],
        [KeyboardButton(text='🚚 Order')]
    ],
    resize_keyboard=True
)

ADMIN_OPTIONS = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='➕ Add'),
            KeyboardButton(text="👁️ All")
        ],
        [KeyboardButton(text='✍️ Update/Delete')],
        [KeyboardButton(text="↩️ Back")]
    ]
)

def admin_category_button():
    inline_keyboard = []
    button = []
    data = get_category()

    for i in range(1,len(data)+1):
        button.append(InlineKeyboardButton(text=data[i-1][1],callback_data=f"admin_category_{data[i-1][0]}"))
        if i %2==0:
            inline_keyboard.append(button)
            button = []

    if button:
         inline_keyboard.append(button)


    inline_keyboard.append([InlineKeyboardButton(text="⬅️ Back", callback_data="admin_category_back")])

    return InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard
    )