from aiogram import Bot, F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import constants as c
import keyboards as k
import states as s
from config import config
from utils import get_weather, get_weather_current_location

bot = Bot(token=config.bot_token.get_secret_value())
router = Router()


@router.message(Command('start'))
async def start(message: types.Message):
    '''Обработка старта'''
    await message.answer(
        text=f'{message.from_user.full_name}, {c.TEXT}',
        reply_markup=k.keyboard
    )


@router.callback_query(StateFilter(None), F.data == 'get')
async def get_city(callback: CallbackQuery, state: FSMContext):
    '''Получение города'''
    await callback.message.answer(
            text='Введите город:',
        )
    await state.set_state(s.Forecast.city)


@router.callback_query(F.data == 'current')
async def get_current(callback: CallbackQuery, state: FSMContext):
    '''Прогноз для теукщего города'''
    response = await get_weather_current_location()
    await callback.message.answer(
        text=f'{response}', reply_markup=k.keyboard_2
    )
    await state.set_state(None)


@router.message(StateFilter(s.Forecast.city))
async def get_city_weather(message: Message, state: FSMContext):
    '''Прогноз для кастомного города'''
    city = message.text
    response = await get_weather(city)
    await message.answer(text=f'{response}', reply_markup=k.keyboard_2)
    await state.set_state(None)


@router.callback_query(StateFilter(None), F.data == 'mm')
async def get_city_next(callback: CallbackQuery, state: FSMContext):
    '''Сброс состояние, нового прогноза'''
    await callback.message.answer(
            text='Введите город:'
        )
    await state.set_state(s.Forecast.city)
    await state.update_data(city=None)
