# -*- coding: utf-8 -*-
r"""flatten_list.py in: 2022-05-01.

Python version: 3.10.0

Escreva uma função que pegue uma lista de listas e a nivele em uma lista
unidimensional.

Nomeie sua função flatten. Ele deve receber um único parâmetro e retornar uma
lista.

Ex.:

flatten([[1, 2], [3, 4]])

Deve retornar a lista:

[1, 2, 3, 4]
"""
from tests.loguru_conf import logger


def flatten(list_of_lists: list) -> list:
    """Obtém uma lista de listas e nivela em uma lista unidimensional.

    Explicação da list comprehension:
    list_ = []
    for sublist in list_of_lists:
        for item in sublist:
            list_.append(item)
    return list_

    :param list_of_lists: lista de listas.
    :type list_of_lists: list
    :return: lista unidimensional.
    :rtype: list
    """
    return [item for sublist in list_of_lists for item in sublist]


def main():
    """Função principal."""
    print(flatten([[1, 2], [3, 4]]))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
