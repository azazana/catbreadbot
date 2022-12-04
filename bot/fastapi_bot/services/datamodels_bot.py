from typing import TypedDict


class Msg(TypedDict):
    msg: str


class History(TypedDict):
    history: list[str]
