import logging
import uuid
from abc import ABC, abstractmethod
from datetime import datetime

import psycopg2
from psycopg2.extras import DictCursor

logger_root = logging.getLogger()


class Storage(ABC):
    """Абстрактный класс хранилища сообщения."""

    @abstractmethod
    def add_message(self, *kwargs) -> str:
        """Получение сообщений."""
        pass

    @abstractmethod
    def set_level(self, user_id, message) -> str:
        """Установить уровень для пользователя."""
        pass

    @abstractmethod
    def get_level(self, user_id) -> str:
        """Получить текущий уровень у пользователя"""
        pass


class MyPostgres(Storage):
    """Postgres class
    initial params:
    """

    def __init__(self, param: dict):
        self.my_connection = psycopg2.connect(**param, cursor_factory=DictCursor)
        self.my_cursor = self.my_connection.cursor()

    def _add_information(self, query, user_id, info):
        try:
            self.my_cursor.execute(query, (str(uuid.uuid4()), user_id, info, datetime.utcnow(),))
        except Exception as err:
            logger_root.error('Error of downloading data in table. Error %s', err)

    def add_message(self, user_id, message) -> None:
        query = f'INSERT INTO telegrambot.history VALUES (%s, %s, %s, %s)'
        self._add_information(query=query, user_id=user_id, info=message)

    def set_level(self, user_id, level) -> None:
        query = f'INSERT INTO telegrambot.level VALUES (%s, %s, %s, %s)'
        self._add_information(query=query, user_id=user_id, info=level)

    def get_level(self, user_id: int) -> int:
        query = f'SELECT * FROM telegrambot.level  level ' \
                f'WHERE level.id_user = (%s) ORDER BY created DESC LIMIT 1'
        row = None
        try:
            self.my_cursor.execute(query, (user_id,))
            row = self.my_cursor.fetchone()
        except Exception as err:
            logger_root.error('Error of reading data in table. Error %s', err)
        if row is None:
            return 0
        else:
            return row[2]
