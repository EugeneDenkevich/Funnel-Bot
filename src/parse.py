import logging
import csv

from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

from parser.create_bot import *


logging.basicConfig(level=logging.INFO)


client.start()


chats = []
last_date = None
size_chats = 200
groups=[]


res = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=size_chats,
    hash=0
))
chats.extend(res.chats)


for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue


print('Выберите группу:')
i = 0

for group in groups:
    print(str(i) + ' - ' + group.title)
    i+=1


group_index = input('Ваш выбор: ')
target_group = groups[int(group_index)]


print('Один момент...')
all = client.get_participants(target_group)


print('Сохранение...')
with open('memders.csv', 'w', encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=',', lineterminator='\n')
    for user in all:
        writer.writerow([user.id])

print('Парсинг участников группы успешно выполнен.')