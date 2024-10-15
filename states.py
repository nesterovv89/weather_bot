from aiogram.fsm.state import State, StatesGroup


class Forecast(StatesGroup):
    city = State()
