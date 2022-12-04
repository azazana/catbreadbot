import logging
import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv
from fastapi_bot.db.MyPostgres import MyPostgres

load_dotenv()
bot = Bot(token=os.environ.get('TOKEN'))
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)
answers = {'start': 'Привет! Я могу тебе отличить кота от хлеба! Объект перед тобой квадратный?',
           'cat': 'Это кот а не хлеб! Не ешь его!',
           'bread': 'Это хлеб, а не кот! Ешь его!',
           'ears': 'У него есть уши?',
           }

dsl = {
    "dbname": os.environ.get("POSTGRES_DB"),
    "user": os.environ.get("POSTGRES_USER"),
    "password": os.environ.get("POSTGRES_PASSWORD"),
    "host": os.environ.get("POSTGRES_HOST"),
    "port": os.environ.get("POSTGRES_PORT"),
}
connection = MyPostgres(param=dsl)


async def start(message: Message):
    connection.set_level(user_id=message.from_id, level=0)
    await message.answer(answers['start'])
    connection.add_message(user_id=message.from_id, message=message.text)


@dp.message_handler(commands=['start'])
async def welcome(message: Message):
    await start(message)


@dp.message_handler(regexp='да|aгa|пожалуй|конечно')
async def yes_cat(message: Message):
    user_id = message.from_id
    text = message.text

    level = connection.get_level(user_id=user_id)
    print(level)
    if level == 0:
        await message.answer(answers['ears'])
        connection.set_level(user_id=user_id, level=level + 1)
    elif level > 0:
        await message.answer(answers['cat'])
        connection.set_level(user_id=user_id, level=-1)
    connection.add_message(user_id=user_id, message=text)


@dp.message_handler(regexp='нет|нет, конечно|ноуп|найн')
async def no_cat(message: Message):
    level = connection.get_level(user_id=message.from_id)
    if level == 0:
        await message.answer(answers['cat'])
    elif level > 0:
        await message.answer(answers['bread'])
    connection.set_level(user_id=message.from_id, level=-1)
    connection.add_message(user_id=message.from_id, message=message.text)
