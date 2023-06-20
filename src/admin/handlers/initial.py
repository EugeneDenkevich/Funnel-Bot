from aiogram import Dispatcher, types

from databases.db import *
from admin.keyboards.hw_work import *


async def get_homeworks(message: types.Message):
    """
    Get a block with homeworks.
    Also we get a markup with an interface for browsing costumer data.
    Get a buttun "Change" for changing a homeworks status.
    """
    count = len(get_homeworks_from_db())
    pagination = InlineKeyboardMarkup(row_width=3)
    left = InlineKeyboardButton('<<', callback_data='left:1')
    right = InlineKeyboardButton('>>', callback_data='right:1')
    counts = InlineKeyboardButton(f'1/{count}', callback_data='count')
    edit = InlineKeyboardButton('Изменить', callback_data='edit')
    pagination.add(edit)
    pagination.add(left, counts, right)
    hw = get_homeworks_from_db()
    await message.answer(f"""
{hw[0].username}\n
ДЗ-1: {hw[0].hw1}
ДЗ-2: {hw[0].hw2}
ДЗ-3: {hw[0].hw3}
""", reply_markup=pagination)


async def hw_process(callback: types.CallbackQuery):
    """
    A process function for browsing customer data.
    Get customer homeworks information and "Change" button for changing homeworks status
    """
    hw = get_homeworks_from_db()
    data = callback.data.split(':')
    if len(data) == 1:
        await callback.answer()
        return
    page = int(data[1])
    count = len(get_homeworks_from_db())
    if data[0] == 'right':
        if page < count:
            page += 1
            pagination = InlineKeyboardMarkup(row_width=3)
            left = InlineKeyboardButton('<<', callback_data=f'left:{page}')
            right = InlineKeyboardButton('>>', callback_data=f'right:{page}')
            counts = InlineKeyboardButton(f'{page}/{count}', callback_data='count')
            edit = InlineKeyboardButton('Изменить', callback_data='edit')
            pagination.add(edit)
            pagination.add(left, counts, right)

            await callback.message.edit_text(f"""
{hw[page-1].username}\n
ДЗ-1: {hw[page-1].hw1}
ДЗ-2: {hw[page-1].hw2}
ДЗ-3: {hw[page-1].hw3}
""", reply_markup=pagination)
            await callback.answer()
        else:
            await callback.answer()
    elif data[0] == 'left':
        if page > 1:
            page -= 1
            pagination = InlineKeyboardMarkup(row_width=3)
            left = InlineKeyboardButton('<<', callback_data=f'left:{page}')
            right = InlineKeyboardButton('>>', callback_data=f'right:{page}')
            counts = InlineKeyboardButton(f'{page}/{count}', callback_data='count')
            edit = InlineKeyboardButton('Изменить', callback_data='edit')
            pagination.add(edit)
            pagination.add(left, counts, right)

            await callback.message.edit_text(f"""
{hw[page-1].username}\n
ДЗ-1: {hw[page-1].hw1}
ДЗ-2: {hw[page-1].hw2}
ДЗ-3: {hw[page-1].hw3}
""", reply_markup=pagination)
            await callback.answer()
        else:
            await callback.answer()
    else:
        await callback.answer()


def register_hanlders(dp: Dispatcher):
    dp.register_message_handler(get_homeworks, commands=['homeworks'])
    dp.register_callback_query_handler(hw_process, lambda callback: True)
