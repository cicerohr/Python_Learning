# -*- coding: utf-8 -*-
"""loguru_conf.py in: 2022-04-18.

Python version: 3.10.0

Settings for loguru-mypy.
"""
from pathlib import Path

from loguru import logger

logger.remove()  # Don't show any logs on console (remove all handlers).

path = Path(__file__).parent.parent

logger.add(
    f'{path}/logs/loguru.log',
    level='DEBUG',
    backtrace=True,
    diagnose=True,
    enqueue=True,
    rotation='1 day',
    retention='10 days',
    format='{time:YYYY-MM-DD HH:mm:ss} | '
    '{level} | {message} | {file} -> {line}',
    # filter=lambda rec: 'api_domain' not in rec['message'].lower(),
)

if __name__ == '__main__':
    print(path)
