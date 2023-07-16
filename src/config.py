from typing import Any, Optional
from logging import getLevelName, INFO

from src.generic.textwrap import hide


class Config:
    __slots__ = 'token', 'username', 'log_level'

    token: str
    username: str
    log_level: int

    def __init__(self, token, username, log_level: Optional[int] = None):
        self.validate_token(token)
        self.validate_username(username)

        self.token = token
        self.username = username
        self.log_level = getLevelName(log_level or INFO)

    def __str__(self) -> str:
        return f"""API Config:
Token: {hide(self.token, 10)}
Username: {self.username}

Logging:
Level: {self.log_level}
"""

    @staticmethod
    def validate_username(value: Any) -> None:
        if not isinstance(value, str):
            raise TypeError("Username must be of str type")

        if not len(value):
            raise ValueError("Username cannot be empty")

    @staticmethod
    def validate_token(value: Any) -> None:
        if not isinstance(value, str):
            raise TypeError("Token must be of str type")

        if not len(value):
            raise ValueError("Token cannot be empty")
