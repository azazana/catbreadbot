import logging
import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.environ.get('TOKEN'))
dp = Dispatcher(bot)

storage = {}
logging.basicConfig(level=logging.INFO)
answers = {'start': 'Привет! Я могу тебе отличить кота от хлеба! Объект перед тобой квадратный?',
           'cat': 'Это кот а не хлеб! Не ешь его!',
           'bread': 'Это хлеб, а не кот! Ешь его!',
           'ears': 'У него есть уши?',
           }


async def start(message: Message):
    storage[message.from_id] = 0
    await message.answer(answers['start'])


@dp.message_handler(commands=['start'])
async def welcome(message: Message):
    await start(message)


@dp.message_handler(regexp='да|aгa|пожалуй|конечно')
async def yes_cat(message: Message):
    level = storage[message.from_id]
    if level == 0:
        await message.answer(answers['ears'])
        storage[message.from_id] += 1
    elif level > 0:
        await message.answer(answers['cat'])
        storage[message.from_id] = -1


@dp.message_handler(regexp='нет|нет, конечно|ноуп|найн')
async def no_cat(message: Message):
    level = storage[message.from_id]
    if level == 0:
        await message.answer(answers['cat'])
    elif level > 0:
        await message.answer(answers['bread'])
    storage[message.from_id] = -1



