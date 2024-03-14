import asyncio
import sys
import logging

from aiogram import Bot, Router, Dispatcher
from aiogram.client.default import DefaultBotProperties

from dotenv import dotenv_values

from database.models import async_main

from handlers import rt
from admin import admin

config = dotenv_values('.env')


async def main():
    await async_main()
    bot = Bot(config['TOKEN'], default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()
    dp.include_routers(rt, admin)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")
