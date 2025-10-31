from aiogram import Bot, Dispatcher
import asyncio
import logging

from handlers import start_router, user_router, admin_router

TOKEN = "8369051789:AAFxh26NyE3dAKhJxEsI41-RZM9g-WUERNs"

dp = Dispatcher()

async def main():
    bot = Bot(token=TOKEN)
    
    dp.include_router(start_router)
    dp.include_router(user_router)
    dp.include_router(admin_router)

    logging.info("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
