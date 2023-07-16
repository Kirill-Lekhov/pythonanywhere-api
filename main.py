#!/usr/bin/env python
from os import environ
from logging import basicConfig

from dotenv import dotenv_values

from src.config import Config
from src.api import API


if __name__ == '__main__':
    env_config = {**dotenv_values('.env'), **environ}
    config = Config(
        username=env_config.get('USERNAME'),
        token=env_config.get('TOKEN'),
        log_level=env_config.get('LOG_LEVEL'),
    )

    basicConfig(level=config.log_level, format="%(levelname)s:%(name)s:↵\n%(message)s")

    api = API(token=config.token, username=config.username)
    api.get_cpu_quota()
    api.delete_file('var/log/kirilllekhov.pythonanywhere.com.access.log')
