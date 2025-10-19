from aiogram import F, Router
from aiogram.types import Message,CallbackQuery,ReplyKeyboardRemove
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
import logging


from states import Register
from texts import START_TEXT, WELCOME_BACK_TEXT
from buttons import (
    START_BUTTONS, PHONE_BUTTON, 
    GENDER_BUTTON, LOCATION_BUTTON, 
    REGISTER_SUCCESS_BUTTONS)
from filters import is_valid_name, is_valid_phone

from database import is_register_by_id, insert_user


start_router = Router()

@start_router.message(CommandStart())
async def start_handler(message:Message):
    if is_register_by_id(message.from_user.id):
        await message.answer(WELCOME_BACK_TEXT, reply_markup=REGISTER_SUCCESS_BUTTONS)
    else:
        await message.answer(START_TEXT,reply_markup=START_BUTTONS)

@start_router.message(F.text == "📝 Ro‘yxatdan o‘tish")
async def register_handler(message:Message, state: FSMContext):
    text = (
    "👋 Salom! Keling, ro‘yxatdan o‘tamiz.\n\n"
    "Ismingizni kiriting (masalan: Aziz Abdusalomov):"
)
    await state.set_state(Register.name)
    await message.answer(text, reply_markup=ReplyKeyboardRemove())

@start_router.message(Register.name)
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

@start_router.message(Register.phone)
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


@start_router.callback_query(F.data.startswith("gender_"))  
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



@start_router.message(Register.address)
async def get_address(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        
        # Получаем адрес
        if message.location:
            lat = message.location.latitude
            lon = message.location.longitude
            address = f"GPS: {lat:.6f}, {lon:.6f}"
        else:
            address = message.text.strip()

        # Сохраняем в базу
        success = insert_user(
            fullname=data["name"],
            phone=data["phone"],
            gender=data["gender"],
            address=address,
            chat_id=message.from_user.id
        )

        if success:
            # Успешное сообщение
            success_text = f"""
🎉 Tabriklaymiz! Ro'yxatdan muvaffaqiyatli o'tdingiz!

📋 Ma'lumotlaringiz:
👤 Ism: {data['name']}
📞 Telefon: {data['phone']}  
⚧ Jins: {data['gender']}
📍 Manzil: {address}
"""
            await message.answer(success_text, reply_markup=REGISTER_SUCCESS_BUTTONS)
        else:
            await message.answer("❌ Ro'yxatdan o'tishda xatolik! Qaytadan urinib ko'ring.")

        await state.clear()

    except Exception as e:
        print(f"Registration error: {e}")
        await message.answer("❌ Xatolik yuz berdi! Iltimos, qaytadan urinib ko'ring.")