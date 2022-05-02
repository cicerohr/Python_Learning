# -*- coding: utf-8 -*-
r"""boolean_and.py in: 2022-05-01.

Python version: 3.10.0

Defina uma função chamada triple_and que receba três parâmetros e retorne True
somente se todos forem True e False caso contrário.
"""
from tests.loguru_conf import logger


def triple_and(a: bool, b: bool, c: bool) -> bool:
    """Função que retorna True se todos forem True e False caso contrário.

    :param a: True or False
    :type a: bool
    :param b: True or False
    :type b: bool
    :param c: True or False
    :type c: bool
    :return: True se todos forem True e False caso contrário
    :rtype: bool
    """
    return a and b and c


def main():
    """Função principal."""
    print(triple_and(True, True, True))
    print(triple_and(True, False, True))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
