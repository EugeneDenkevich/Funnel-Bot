import os
from datetime import datetime, timedelta

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from databases.db import *
from client.utils.timers.timers import *
from client.keyboards.send_hw import *


async def send_welcome(message: types.Message):
    with open(os.path.join('media', 'start.jpg'), 'rb') as photo:
        await message.answer_photo(photo=photo,
                                   caption=f"""
Привет, {message.from_user.full_name} 👋
Это Игровая Воронка, в которой у тебя есть 3 жизни. ❤❤❤
Жизнь сгорает через 8 часов после того, как тебе была выслана домашка.
Если ты сделал домашку раньше, чем сгорела очередная жизнь - тогда счётик обновляется, но жизни не восстанавливаются.

Для того, чтобы дойти до конца, тебе нужно сделать 3 домашки.
Каждую домашку отправляй мне в ЛС.
Если ты готов, можем приступить.
⬇️⬇️⬇️
""", reply_markup=send_hw1)
    set_user(message.from_user.id, message.from_user.full_name)
    timer = AsyncIOScheduler()
    timer.add_job(check_start, 'date', run_date=datetime.now() +
                  timedelta(seconds=INIT_TIMER), kwargs={'message': message})
    timer.start()


async def get_hw1(callback: types.CallbackQuery):
    hw_status = check_hw1(callback.from_user.id)
    if hw_status == 'disactive':
        activate_hw1(callback.from_user.id)
        await callback.message.answer("""
🌼 Вот ваше ДЗ1 ⬇️
Скопируй его и допиши слово "Индустриализация".
""")
        await callback.message.answer(f"""
Ваш ИД-{get_system_id(callback.from_user.id)}

Мой первый слог сидит в чалме,
Он на Востоке быть обязан.
Второй же слог известен мне,
Он с цифрою как будто связан.

В чалме сидит и третий слог,
Живет он тоже на Востоке.
Четвертый слог поможет бог
Узнать, что это есть предлог.

Ответ:
""", reply_markup=ask_expert)
        await callback.answer()
    elif hw_status == 'active':
        await callback.message.answer('☝🏼 ДЗ1 уже было выслано',
                                      reply_markup=resend_hw1_k)
        await callback.answer()
    elif hw_status == 'done':
        await callback.message.answer('✅ ДЗ1 уже было сделано')
        await callback.answer()


async def resend_hw1(callback: types.CallbackQuery):
    await callback.message.answer("""
🌼 Вот ваше ДЗ1 ⬇️
Скопируйте его и допишите слово "Индустриализация".
""")
    await callback.message.answer(f"""
Ваш ИД-{get_system_id(callback.from_user.id)}

Мой первый слог сидит в чалме,
Он на Востоке быть обязан.
Второй же слог известен мне,
Он с цифрою как будто связан.

В чалме сидит и третий слог,
Живет он тоже на Востоке.
Четвертый слог поможет бог
Узнать, что это есть предлог.

Ответ:
""", reply_markup=ask_expert)
    await callback.answer()


async def get_hw(message: types.Message):
    if get_system_id(message.from_user.id) in message.text:
        await message.answer(f'Спасибо за то, что выслали {get_hw_number(message.from_user.id)}')


def register_hanlders(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_callback_query_handler(get_hw1, Text('hw1'))
    dp.register_callback_query_handler(
        resend_hw1, Text('resend_hw1'))
    dp.register_message_handler(get_hw)
