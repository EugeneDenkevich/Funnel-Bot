from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from admin.data.config import TOKEN_ADMIN


starage = MemoryStorage()
bot = Bot(token=TOKEN_ADMIN)
dp = Dispatcher(bot, storage=starage)
