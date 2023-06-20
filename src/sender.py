import logging

from aiogram import executor

from sender.create_bot import bot, dp
from sender.handlers.bot_sender import *


logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp, skip_updates=True)
