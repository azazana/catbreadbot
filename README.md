# Тестовое задание 

![img.png](img.png)

Запуск локально:
Запускаем докер для postgresql:

`docker run -d \
  --name catbread-postgres-1 \
  -p 5432:5432 \
  -v $HOME/postgresql/data:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=123qwe \
  -e POSTGRES_USER=app \
  -e POSTGRES_DB=telegrambot  \
  postgres:13` 


`docker exec -it catbread-postgres-1 bash`


`psql -h 127.0.0.1 -U app -d telegrambot` 

python -m pytest tests
http://0.0.0.0:8000/api/cat_bread_bot/3345/да

Запуск в докер-компоуз