from telethon.sync import TelegramClient
from parser.data.config import *


api_id = API_ID
api_hash = API_HASH
phone = PHONE
client = TelegramClient(phone, api_id, api_hash)
