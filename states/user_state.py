from aiogram.fsm.state import State, StatesGroup


class MenuOption(StatesGroup):
    gender = State()
    category = State()
    season = State()
    