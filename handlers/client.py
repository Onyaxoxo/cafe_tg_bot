from aiogram import Dispatcher, types  
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


###**************************** КЛИЕНТСКАЯ ЧАСТЬ ****************************###
# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Приятного аппетита!", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общеине с ботом доступно только в Личных сообщениях, пожалуйста, напишите ему: \nhttps://t.me/pokibot_bot")

# @dp.message_handler(commands=['Режим_работы'])
async def open_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Добавить время работы") #, reply_markup=ReplyKeyboardRemove()

# @dp.message_handler(commands=['Расположение'])
async def place_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Добавить адрес") #, reply_markup=ReplyKeyboardRemove()

@dp.message_handler(commands=['Меню'])
async def menu_command(message: types.Message):
    await sqlite_db.sql_read(message)
    

# функция для передачи handlers в основной файл 
def registr_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start','help'])
    dp.register_message_handler(open_command, commands=['Режим_работы'])
    dp.register_message_handler(place_command, commands=['Расположение'])
    dp.register_message_handler(menu_command, commands=['Меню'])
