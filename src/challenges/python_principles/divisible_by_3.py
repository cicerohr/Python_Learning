# -*- coding: utf-8 -*-
r"""divisible_by_3.py in: 2022-05-01.

Python version: 3.10.0

Defina uma função chamada div_3 que retorne True se seu único parâmetro inteiro
for divisível por 3 e False caso contrário.

Por exemplo, div_3(6) é True porque 6/3 não deixa nenhum resto. No entanto,
div_3(5) é False porque 5/3 deixa 2 como resto.
"""
from tests.loguru_conf import logger


def div_3(num: int) -> bool:
    """Função para verificar se um número é divisível por 3.

    :param num: número a ser verificado.
    :type num: int
    :return: True se o número for divisível por 3. False caso contrário.
    :rtype: bool
    """
    return num % 3 == 0


def main():
    """Função principal."""
    print(div_3(6))
    print(div_3(5))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
