from aiogram.fsm.state import State, StatesGroup


class MenuAdmin(StatesGroup):
    category = State()
    field = State()
    