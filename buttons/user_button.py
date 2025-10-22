from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# --- GENDER BUTTONS ---
GENDER_BUTTONS = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🧔 Erkaklar uchun", callback_data="menu_gender_male")],
        [InlineKeyboardButton(text="👩 Ayollar uchun", callback_data="menu_gender_female")],
        [InlineKeyboardButton(text="🧒 Bolalar uchun", callback_data="menu_gender_child")],
        [InlineKeyboardButton(text="⏪ Orqaga", callback_data="menu_gender_back")],
    ]
)


# --- CATEGORY BUTTONS ---
CATEGORY_BUTTONS = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👕 Koylak (Shirt)", callback_data="category_shirt"),
            InlineKeyboardButton(text="🧢 Kepka (Cap)", callback_data="category_cap"),
        ],
        [
            InlineKeyboardButton(text="👟 Krossovkalar (Shoes)", callback_data="category_shoes"),
            InlineKeyboardButton(text="🧥 Kurtka (Jacket)", callback_data="category_jacket"),
        ],
        [
            InlineKeyboardButton(text="👖 Shimlar (Trousers)", callback_data="category_trousers"),
            InlineKeyboardButton(text="💍 Aksessuar (Accessory)", callback_data="category_accessory"),
        ],
        [
            InlineKeyboardButton(text="🤵 Kostyum (Suit)", callback_data="category_suit"),
            InlineKeyboardButton(text="👜 Sumka (Bag)", callback_data="category_bag"),
        ],
        [
            InlineKeyboardButton(text="🔙 Orqaga (Back)", callback_data="category_back"),
        ],
    ]
)


# --- SEASON BUTTONS ---
SEASON_BUTTONS = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="☀️ Yoz (Summer)", callback_data="season_summer"),
            InlineKeyboardButton(text="🍂 Kuz (Autumn)", callback_data="season_autumn"),
        ],
        [
            InlineKeyboardButton(text="❄️ Qish (Winter)", callback_data="season_winter"),
            InlineKeyboardButton(text="🌸 Bahor (Spring)", callback_data="season_spring"),
        ],
        [
            InlineKeyboardButton(text="🔙 Orqaga", callback_data="season_back"),
        ],
    ]
)
