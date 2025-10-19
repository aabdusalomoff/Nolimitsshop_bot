from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.types.input_file import FSInputFile 

from texts import GENDER_TEXT

from buttons import GENDER_BUTTON

user_router = Router()


@user_router.message(F.text == "📋 Menu")
async def start_menu(message:Message):

    image_path = "media/image/b17390ccf852a453f2b05817a4fc8a38.jpg"
    await message.answer_photo(photo=FSInputFile(path=image_path),caption=GENDER_TEXT,reply_markup=GENDER_BUTTON)

    await message.answer("Siz menuni tanladingiz")

