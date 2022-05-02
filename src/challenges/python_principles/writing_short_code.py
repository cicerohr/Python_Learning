# -*- coding: utf-8 -*-
r"""writing_short_code.py in: 2022-05-01.

Python version: 3.10.0

Defina uma função chamada convert que receba uma lista de números como seu
único parâmetro e retorne uma lista de cada número convertido em uma ‘string’.

Por exemplo, a chamada convert([1, 2, 3]) deve retornar ["1", "2", "3"].

O que torna isso complicado é que o corpo da sua função deve conter apenas uma
única linha de código.
"""
from tests.loguru_conf import logger

# def convert(numbers: list) -> list:
#     """Converte uma lista de números em uma lista de ‘strings’.
#
#     :param numbers: lista de números.
#     :type numbers: list
#     :return: lista de strings convertida.
#     :rtype: list
#     """
#     return [str(numero) for numero in numbers]

convert = lambda numbers: [str(numero) for numero in numbers]


def main():
    """Função principal."""
    print(convert([1, 2, 3]))
    print(convert([4, 5, 6]))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
