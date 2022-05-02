# -*- coding: utf-8 -*-
r"""consecutive_zeros.py in: 2022-05-01.

Python version: 3.10.0

O objetivo deste desafio é analisar uma ‘string’ binária consistindo apenas de
zeros e uns. Seu código deve encontrar o maior número de zeros consecutivos na
‘string’. Por exemplo, dada a string:

"1001101000110"

O maior número de zeros consecutivos é 3.

Defina uma função chamada consecutiva_zeros que recebe um único parâmetro,
sendo a sequência de zeros e uns.

Sua função deve retornar o número descrito acima.
"""
from itertools import groupby

from tests.loguru_conf import logger


def consecutiva_zeros(string: str) -> int:
    """Função que retorna o número de zeros consecutivos.

    :param string: string de zeros e uns.
    :type string: str
    :return: maior número de zeros consecutivos.
    :rtype: int
    """
    # maior = cont = 0
    # for _, c in enumerate(string):
    #     if c == '0':
    #         cont += 1
    #         if cont > maior:
    #             maior = cont
    #     else:
    #         cont = 0
    # return maior

    return max(
        len(list(value)) for key, value in groupby(string) if key == '0'
    )


def main():
    """Função principal."""
    print(consecutiva_zeros('1001101000110'))
    print(consecutiva_zeros('1000000111111'))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
