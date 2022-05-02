# -*- coding: utf-8 -*-
r"""thousands_separator.py in: 2022-05-02.

Python version: 3.10.0

Escreva uma função chamada format_number que receba um número não negativo como
seu único parâmetro.

Sua função deve converter o número em uma ‘string’ e adicionar vírgulas como
separador de milhares.

Por exemplo, chamar format_number(1000000) deve retornar '1,000,000'.
"""
from tests.loguru_conf import logger


def format_number(number: int) -> str:
    """Função que formata um número.

    :param number: número a ser formatado.
    :type number: int
    :return: ‘string’ com o número formatado.
    :rtype: str
    """
    return f'{number:,}'


def main():
    """Função principal."""
    print(format_number(1000000))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
