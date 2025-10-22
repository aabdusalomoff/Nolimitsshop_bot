from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.types.input_file import FSInputFile 

from texts import GENDER_TEXT, CATEGORY_TEXT, SEASON_TEXT

from buttons import GENDER_BUTTONS,REGISTER_SUCCESS_BUTTONS, CATEGORY_BUTTONS, SEASON_BUTTONS
from states import MenuOption

user_router = Router()


@user_router.message(F.text == "📋 Menu")
async def start_menu(message:Message,state:FSMContext):

    await state.set_state(MenuOption.gender)

    image_path = "media/image/b17390ccf852a453f2b05817a4fc8a38.jpg"
    await message.answer_photo(photo=FSInputFile(path=image_path),caption=GENDER_TEXT,reply_markup=GENDER_BUTTONS, parse_mode="HTML")

@user_router.callback_query(F.data.startswith("menu_gender_"))
async def get_gender_menu(call:CallbackQuery,state:FSMContext):
    gender = call.data.split("_")[-1]

    if gender == "back":
        await state.clear()
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer(GENDER_TEXT,reply_markup=REGISTER_SUCCESS_BUTTONS)
    else:
        await state.update_data(gender=gender)
        await state.set_state(MenuOption.category)
       
        await call.message.edit_caption(caption=CATEGORY_TEXT)
        await call.message.edit_reply_markup(reply_markup=CATEGORY_BUTTONS)


@user_router.callback_query(F.data.startswith("category_"))
async def get_category_menu(call:CallbackQuery,state:FSMContext):
    category = call.data.split("_")[-1]

    if category == "back":
        await call.message.answer(caption=GENDER_TEXT, parse_mode="HTML")
        await call.message.edit_reply_markup(reply_markup=GENDER_BUTTONS)
    else:

        await state.update_data(category=category)
        await state.set_state(MenuOption.season)

        await call.message.edit_caption(text=SEASON_TEXT)
        await call.message.edit_reply_markup(reply_markup=SEASON_BUTTONS)
        
@user_router.callback_query(F.data.startswith("season_"))
async def send_product_by_filter(call:CallbackQuery,state:FSMContext):
    season = call.data.split("_")[-1]

    if season == "back":
        await call.message.edit_caption(caption=CATEGORY_TEXT)
        await call.message.edit_reply_markup(reply_markup=CATEGORY_BUTTONS)
    else:

        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer(f"Siz gender")