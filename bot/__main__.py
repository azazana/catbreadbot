from bot.handlers import cat_bread_bot
from aiogram.utils import executor

if __name__ == '__main__':
    executor.start_polling(cat_bread_bot.dp, skip_updates=True)
