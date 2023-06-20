import logging

from aiogram import executor

from client.create_bot import bot, dp
from client.utils.set_bot_commands import set_bot_default_commands
import client.handlers.initial as initial


logging.basicConfig(level=logging.INFO)


async def start_bot(*args):
    await set_bot_default_commands(bot)


if __name__ == "__main__":
    initial.register_hanlders(dp)
    executor.start_polling(
        dispatcher=dp, skip_updates=True, on_startup=start_bot)
