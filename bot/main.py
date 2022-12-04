import uvicorn
from fastapi.responses import ORJSONResponse

from fastapi import FastAPI
from fastapi_bot.api.api_bot import router

app = FastAPI(
    title='cat bread bot',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

# Подключаем роутер к серверу, указав префикс /v1/films
# Теги указываем для удобства навигации по документации
app.include_router(router, prefix='/api/cat_bread_bot', tags=['bot'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
    )
