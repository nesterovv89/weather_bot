import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

import handlers
from config import config

load_dotenv()

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()


async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_routers(handlers.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
