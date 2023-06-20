import time
import traceback

from aiogram.types.input_file import InputFile
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from sender.create_bot import *


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db_sender.user_exists(message.from_user.id):
            db_sender.add_user(message.from_user.id)
        await message.answer('Welcome')


@dp.message_handler(commands=['sendall'])
async def sendall(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 5508567586:
            print('\n\n---> Achtung! Mailing gestartet!\n\n')
            users = db_sender.get_users()[:30]
            reply_markup = InlineKeyboardMarkup(row_width=1)
            reply_markup.add(InlineKeyboardButton(text='🦑 Перейти в ЛС', url='https://t.me/OliyaErmakova'))
            for i in range(len(users)):
                if i % 28 == 0:
                    time.sleep(WAIT)
                    try:
                        with open(PICTURE_PATH, 'rb') as file:
                            await bot.send_photo(chat_id=users[i][0], photo=file, caption=TEXT, reply_markup=reply_markup)
                            if int(users[i][1]) != 1:
                                db_sender.set_active(users[i][0], 1)
                    except Exception as e:
                        db_sender.set_active(users[i][0], 0)
                        print(traceback.format_exc())
                else:
                    try:
                        with open(PICTURE_PATH, 'rb') as file:
                            await bot.send_photo(chat_id=users[i][0], photo=file, caption=TEXT, reply_markup=reply_markup)
                            if int(users[i][1]) != 1:
                                db_sender.set_active(users[i][0], 1)
                    except:
                        db_sender.set_active(users[i][0], 0)
                        print(traceback.format_exc())
            print('---> Success!')