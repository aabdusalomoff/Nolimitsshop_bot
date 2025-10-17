from aiogram import Bot, Dispatcher, F
from environs import Env
import logging

import asyncio

from handlers import start_router


env = Env()
env.read_env()

dp = Dispatcher()
TOKEN = env.str("TOKEN")


async def main():
    bot = Bot(TOKEN)
    dp.include_router(start_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
