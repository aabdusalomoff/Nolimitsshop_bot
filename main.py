from aiogram import Bot, Dispatcher, F
from aiogram.types import Message,ReplyKeyboardRemove,CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from environs import Env
import logging

import asyncio


from text_bot import START_TEXT
from buttons import (
    START_BUTTONS, PHONE_BUTTON, 
    GENDER_BUTTON, LOCATION_BUTTON,REGISTER_SUCCESS_BUTTONS)
from filter import is_valid_name, is_valid_phone
from states import Register

env = Env()
env.read_env()

dp = Dispatcher()
TOKEN = env.str("TOKEN")

@dp.message(CommandStart())
async def start_handler(message:Message):
    await message.answer(START_TEXT,reply_markup=START_BUTTONS)

@dp.message(F.text == "📝 Ro‘yxatdan o‘tish")
async def register_handler(message:Message, state: FSMContext):
    text = (
    "👋 Salom! Keling, ro‘yxatdan o‘tamiz.\n\n"
    "Ismingizni kiriting (masalan: Aziz Abdusalomov):"
)
    await state.set_state(Register.name)
    await message.answer(text, reply_markup=ReplyKeyboardRemove())

@dp.message(Register.name)
async def get_name(message:Message,state:FSMContext):
    try:
        full_name = message.text
        if is_valid_name(full_name):
            await state.update_data(name=message.text)
            await state.set_state(Register.phone)
            await message.answer(
    "✅ Ismingiz qabul qilindi!\n\n"
    "📱 Endi telefon raqamingizni yuboring.\n"
    "Masalan: +998901234567 yoki quyidagi tugmadan foydalaning 👇",
    reply_markup=PHONE_BUTTON
)
        else:
            await message.answer("❌ Iltimos, to'g'ri formatda ism kiriting (2-50 belgi)")
    except Exception as e:
        logging.error(f"Name error: {e}")
        await message.answer("❌ Xatolik yuz berdi, qaytadan urining")

@dp.message(Register.phone)
async def get_phone(message:Message,state:FSMContext):
    try:
        if message.contact:
            phone = message.contact.phone_number
        else:
            phone = message.text.strip()
        
        if not is_valid_phone(phone):
            error_text = """
❌ Noto'g'ri telefon raqam formati!

✅ To'g'ri formatlar:
• +998901234567
• 998901234567  
• 901234567

Iltimos, qaytadan kiriting:
            """
            await message.answer(error_text, reply_markup=PHONE_BUTTON)
            return
        
        if phone.startswith('+'):
            normalized_phone = phone
        elif phone.startswith('998'):
            normalized_phone = '+' + phone
        else:  
            normalized_phone = '+998' + phone[1:] if phone.startswith('9') else '+998' + phone
        
        await state.update_data(phone=normalized_phone)
        await state.set_state(Register.gender)
        
        await message.answer(f"✅ Telefon raqam qabul qilindi: {normalized_phone}", 
                           reply_markup=ReplyKeyboardRemove())
        await message.answer("⚧ Jinsingizni tanlang:", reply_markup=GENDER_BUTTON)
        
    except Exception as e:
        logging.error(f"Phone validation error: {e}")
        await message.answer("❌ Xatolik yuz berdi, qaytadan urining:", 
                           reply_markup=PHONE_BUTTON)


@dp.callback_query(F.data.startswith("gender_"))  
async def get_gender(call:CallbackQuery, state:FSMContext):
    gender = call.data.split("_")[-1]
    await state.update_data(gender=gender)
    await state.set_state(Register.address)
    
    await call.answer(f"Siz {gender} ni tanladingiz")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(
    "📍 Manzilingizni yuboring.\n\n"
    "Agar GPS yoqilgan bo‘lsa, pastdagi tugmani bosing.\n"
    "Yoki manzilni yozma shaklda yuboring (masalan: Farg‘ona, Marg‘ilon yo‘li 12).",
    reply_markup=LOCATION_BUTTON
)



@dp.message(Register.address)
async def get_address(message: Message, state: FSMContext):
    data = await state.get_data()

    if message.location:
        lat = message.location.latitude
        lon = message.location.longitude
        address = f"{lat}, {lon}"
    else:
        address = message.text.strip()

    data["address"] = address

    success_text = f"""
🎉 Tabriklaymiz, siz muvaffaqiyatli ro‘yxatdan o‘tdingiz!

📋 Siz haqingizdagi ma’lumotlar:
👤 Ism: {data['name']}
📞 Telefon: {data['phone']}
⚧ Jins: {data['gender']}
📍 Manzil: {address}

Endi siz bizning to‘liq foydalanuvchimizsiz 💪  
🛍️ Buyurtma berish uchun “Menu” tugmasini bosing!
"""


    await message.answer(success_text, reply_markup=REGISTER_SUCCESS_BUTTONS)
    await state.clear()


async def main():
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
