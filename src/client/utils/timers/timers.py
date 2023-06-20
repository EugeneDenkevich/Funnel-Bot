from databases.db import *

from aiogram import types

# All timers in seconds!
INIT_TIMER = 10


async def check_start(message: types.Message):
    if check_hw1(message.from_user.id) == 'disactive':
        await message.answer(f"""
Это напоминание.
Вы его видите, так как {INIT_TIMER} секунд не нажимали на кнопку "Получить ДЗ1"
""")
