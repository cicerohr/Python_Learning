# -*- coding: utf-8 -*-
r"""capital_indexes.py in: 2022-04-30.

Python version: 3.10.0
"""
from tests.loguru_conf import logger


def capital_indexes(string: str) -> list:
    """Função capital_indexes.

    A função leva um único parâmetro, uma ‘string’. Sua função deve
    retornar uma lista de todos os índices da sequência com letras
    maiúsculas.

    Por exemplo, chamar capital_indexes ("HeLlO") deve retornar a
    lista [0, 2, 4].

    :param string: string a ser analisada.
    :type string: str
    :return: lista de índices das letras maiúsculas.
    :rtype: list
    """
    return [indice for indice, valor in enumerate(string) if valor.isupper()]


def main():
    """Main function."""
    print(capital_indexes('HeLlO'))
    print(capital_indexes('HeLlO World'))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
