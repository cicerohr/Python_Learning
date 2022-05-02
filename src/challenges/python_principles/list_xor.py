# -*- coding: utf-8 -*-
r"""list_xor.py in: 2022-05-02.

Python version: 3.10.0

Defina uma função chamada list_xor. Sua função deve ter três parâmetros: n,
list1 e list2.

Sua função deve retornar se n está exclusivamente em list1 ou list2.

Em outras palavras, se n estiver em ambas as listas ou em nenhuma das listas,
retorne False. Se n estiver em apenas uma das listas, retorne True.

Por exemplo:

list_xor(1, [1, 2, 3], [4, 5, 6]) == True
list_xor(1, [0, 2, 3], [1, 5, 6]) == True
list_xor(1, [1, 2, 3], [1, 5, 6]) == False
list_xor(1, [0, 0, 0], [4, 5, 6]) == False
"""
from tests.loguru_conf import logger


def list_xor(n: int, list1: list, list2: list) -> bool:
    """Função que retorna se n está exclusivamente em list1 ou list2.

    :param n: intero a ser verificado.
    :type n: int
    :param list1: lista de inteiros.
    :type list1: list
    :param list2: lista de inteiros.
    :type list2: list
    :return: True se n está exclusivamente em list1 ou list2.
    :rtype: bool
    """
    return (n in list1) ^ (n in list2)


def main():
    """Função principal."""
    print(list_xor(1, [1, 2, 3], [4, 5, 6]))
    print(list_xor(1, [0, 2, 3], [1, 5, 6]))
    print(list_xor(1, [1, 2, 3], [1, 5, 6]))
    print(list_xor(1, [0, 0, 0], [4, 5, 6]))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
