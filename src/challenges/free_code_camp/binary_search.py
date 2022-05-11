# -*- coding: utf-8 -*-
r"""binary_search.py in: 2022-05-11.

@author: Kylie Ying
@link: https://www.youtube.com/watch?v=8ext9G7xspg&t=4553s
"""
from tests.loguru_conf import logger


def binary_search(arr, target):
    """Função que busca um elemento em um array.

    A função recebe um array e um elemento e retorna o índice do elemento
    se ele estiver no array.

    Caso o elemento não esteja no array, retorna -1.

    :param arr: lista com os elementos a serem buscados.
    :type arr: list
    :param target: elemento a ser buscado.
    :type target: int
    :return: índice do elemento buscado.
    :rtype: int
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    """Função principal."""
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
