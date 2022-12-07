from unittest.mock import AsyncMock, patch

import pytest

from bot.handlers.cat_bread_bot import welcome, answers, no_cat, yes_cat

mes = {'from_id': '123'}


@pytest.mark.asyncio
async def test_start():
    message = AsyncMock(**mes)
    await welcome(message)
    message.answer.assert_called_with(answers['start'])


@pytest.mark.asyncio
async def test_yes_cat(monkeypatch):
    with patch('bot.handlers.cat_bread_bot.connection.get_level',
               return_value=0):
        mes['text'] = answers['ears']
        message_mock = AsyncMock(**mes)
        await yes_cat(message=message_mock)
        message_mock.answer.assert_called_with(mes['text'])
    with patch('bot.handlers.cat_bread_bot.connection.get_level',
               return_value=1):
        mes['text'] = answers['cat']
        await yes_cat(message=message_mock)
        message_mock.answer.assert_called_with(mes['text'])


@pytest.mark.asyncio
@patch('bot.handlers.cat_bread_bot.connection.get_level', return_value=0)
async def test_no_cat(monkeypatch):
    with patch('bot.handlers.cat_bread_bot.connection.get_level',
               return_value=0):
        message_mock = AsyncMock(**mes)
        await no_cat(message=message_mock)
        message_mock.answer.assert_called_with(mes['text'])
    with patch('bot.handlers.cat_bread_bot.connection.get_level',
               return_value=1):
        mes['text'] = answers['bread']
        await no_cat(message=message_mock)
        message_mock.answer.assert_called_with(mes['text'])
