from aiogram.fsm.state import State, StatesGroup


class Register(StatesGroup):
    name = State()
    phone = State()
    gender = State()
    address = State()