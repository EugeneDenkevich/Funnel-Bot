from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from client.data.config import EXPERT_URL


send_hw1 = InlineKeyboardMarkup(row_width=1)
send = InlineKeyboardButton('Получить ДЗ1', callback_data='hw1')
send_hw1.add(send)


ask_expert = InlineKeyboardMarkup(row_width=1)
go_to = InlineKeyboardButton(
    '📝Задать вопросы эксперту', url=EXPERT_URL)
ask_expert.add(go_to)

resend_hw1_k = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(f'🔁 Выслать ДЗ1 снова', callback_data='resend_hw1'))
