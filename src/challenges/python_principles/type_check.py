# -*- coding: utf-8 -*-
r"""type_check.py in: 2022-05-01.

Python version: 3.10.0

Escreva uma função chamada only_ints que receba dois parâmetros.
Sua função deve retornar True se ambos os parâmetros forem inteiros e
False caso contrário.
"""
from typing import Any

from tests.loguru_conf import logger


def only_ints(a: Any, b: Any) -> bool:
    """
    Verifica se os dois parâmetros são inteiros.

    :param a: primeiro parâmetro.
    :type a: Any.
    :param b: segundo parâmetro.
    :type b: Any.
    :return: True se os dois parâmetros são inteiros e False caso contrário.
    :rtype: bool
    """
    if isinstance(a, int) and isinstance(b, int):
        return True
    return False


def main():
    """Função principal."""
    print(only_ints(1, 2))
    print(only_ints(1, 2.0))
    print(only_ints('1', '2'))
    print(only_ints('1', 2))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
