from typing import Any

from fastapi import APIRouter, Request

router = APIRouter()


@router.get('/{user_id}/{message}',
            summary='api для котохлебобота')
async def post_message(request: Request, user_id: str, message: str) -> Any:
    pass
