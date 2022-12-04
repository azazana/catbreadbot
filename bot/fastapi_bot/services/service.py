from bot.handlers.cat_bread_bot import yes_cat_handler


async def get_message_from_bot(user_id: str, message: str):
    if message == 'да':
        return await yes_cat_handler(user_id=user_id, message=message)
