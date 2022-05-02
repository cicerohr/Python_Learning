# -*- coding: utf-8 -*-
r"""randomness.py in: 2022-05-01.

Python version: 3.10.0

Defina uma função, random_number, que não requer parâmetros. A função deve
gerar um inteiro aleatório entre 1 e 100, inclusive, e devolvê-lo.
Chamar a função várias vezes deve (geralmente) retornar números diferentes.
"""
from tests.loguru_conf import logger


def random_number() -> int:
    """
    Gera um número aleatório entre 1 e 100, inclusive.

    :return: um inteiro aleatório entre 1 e 100, inclusive.
    :rtype: int
    """
    from random import randint

    return randint(1, 100)


def main():
    print(random_number())


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
