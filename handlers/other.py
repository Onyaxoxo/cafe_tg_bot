from aiogram import types, Dispatcher 
import json
import string
from create_bot import dp

# @dp.message_handler()
async def echo_send(message : types.Message):
    # await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text) # сообщение от бота в личку (если пользователь писал до этого боту)

# фильтр мата (генератор множеств)
#  
    if {i.lower().translate(str.maketrans('','', string.punctuation)) for i in message.text.split(" ")}\
        .intersection(set(json.load(open('C:\\Users\\Onyaxoxo\\MyDrive\\PyCharm\\tgbot\\cenz.json')))) != set():
        await message.reply('Пожалуйста, без мата')
        await message.delete()

def registr_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)