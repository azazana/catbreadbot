from unittest.mock import AsyncMock

import pytest

from bot.handlers import cat_bread_bot
from bot.handlers.cat_bread_bot import start, answers, no_cat, yes_cat

mes = {'from_id': '123'}


@pytest.mark.asyncio
async def test_start():
    message = AsyncMock(**mes)
    await start(message)
    message.answer.assert_called_with(answers['start'])


@pytest.mark.asyncio
async def test_yes_cat(monkeypatch):
    monkeypatch.setattr(cat_bread_bot, "storage", {mes['from_id']: 0})
    mes['text'] = answers['ears']
    message_mock = AsyncMock(**mes)
    await yes_cat(message=message_mock)
    message_mock.answer.assert_called_with(mes['text'])
    mes['text'] = answers['cat']
    await yes_cat(message=message_mock)
    message_mock.answer.assert_called_with(mes['text'])


@pytest.mark.asyncio
async def test_no_cat(monkeypatch):
    monkeypatch.setattr(cat_bread_bot, "storage", {mes['from_id']: 0})
    mes['text'] = answers['cat']
    message_mock = AsyncMock(**mes)
    await no_cat(message=message_mock)
    message_mock.answer.assert_called_with(mes['text'])
    monkeypatch.setattr(cat_bread_bot, "storage", {mes['from_id']: 1})
    mes['text'] = answers['bread']
    await no_cat(message=message_mock)
    message_mock.answer.assert_called_with(mes['text'])