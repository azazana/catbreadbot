import os
from typing import Any
from fastapi import APIRouter, Request, requests

router = APIRouter()


# @router.get('/{user_id}/{message}',
#              summary='api для котохлебобота')
# async def post_message(request: Request, user_id: str, message: str) -> Any:
#     '''
#     Получить ответ от котохлебобота
#     :param request:
#     :param user_id: ID пользоваться
#     :param message: Сообщение от пользователя
#     :return: ответ от бота
#     '''
#
#     return await get_message_from_bot(user_id=user_id, message=message)

@router.get('/{user_id}/{message}',
            summary='api для котохлебобота')
async def post_message(request: Request, user_id: str, message: str) -> Any:
    pass
    # '''
    # Получить ответ от котохлебобота
    # :param request:
    # :param user_id: ID пользоваться
    # :param message: Сообщение от пользователя
    # :return: ответ от бота
    # '''
    # url = 'https://api.telegram.org/bot{}/sendMessage'.format(os.environ.get('TOKEN'))
    #
    # params = {
    #     'chat_id': os.environ.get('CHAT_ID'),
    #     'text': message,
    #     'user_id': user_id,
    #     'disable_web_page_preview': True,
    #     'protect_content': True
    # }
    # r=request.get(url=url, params=params)
    # # r = requests.get(url, params=params)
    #
    # return {"message": "Message sent successfully."}
