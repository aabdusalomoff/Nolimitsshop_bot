from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.types.input_file import FSInputFile 
from aiogram.filters import Command 

from database import is_admin_by_id,is_register_by_id

from buttons import ADMIN_REGISTER,ADMIN_MENU, ADMIN_OPTIONS,admin_category_button

from states import MenuAdmin


admin_router = Router()



@admin_router.message(Command('admin'))
async def start_admin(message:Message):

    if is_register_by_id(message.from_user.id):
        if is_admin_by_id(message.from_user.id):
            await message.answer("admin panelga xush kelibsiz!!!",reply_markup=ADMIN_MENU)
        else:
            await message.answer("Siz admin emassiz!!")
    else:
        await message.answer("Avval royxatdan o'ting:",reply_markup=ADMIN_REGISTER)



@admin_router.message(F.text=="🧾 Menu")
async def start_menu_admin(message:Message,state:FSMContext):

    image_path = 'media/image/menu.jpg'
    await state.set_state(MenuAdmin.category)

    await message.answer_photo(photo=FSInputFile(path=image_path),caption="Menulardan birini tanlang:",reply_markup=admin_category_button())


@admin_router.callback_query(F.data.startswith("admin_category"))
async def get_category_admin(call:CallbackQuery,state:FSMContext):

    category = call.data.split("_")[-1]

    await call.message.edit_caption(caption=f"{category} tanlang: ")
    await call.message.answer("Menu tanlang: ",reply_markup=ADMIN_OPTIONS)
   



