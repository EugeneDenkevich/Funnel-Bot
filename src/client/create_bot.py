from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from client.data.config import TOKEN_CLIENT


starage = MemoryStorage()
bot = Bot(token=TOKEN_CLIENT)
dp = Dispatcher(bot, storage=starage)

