# -*- coding: utf-8 -*-
r"""min_maxing.py in: 2022-05-01.

Python version: 3.10.0

Defina uma função chamada large_difference que recebe uma lista de números como
seu único parâmetro.

Sua função deve calcular e retornar a diferença entre o maior e o menor número
da lista.

Por exemplo, a chamada large_difference([1, 2, 3]) deve retornar 2 porque
(3 – 1) é 2.

Você pode assumir que nenhum número é menor ou maior que -100 e 100
respectivamente.
"""
from tests.loguru_conf import logger


def large_difference(numbers: list) -> float | int:
    """Calcula a diferença entre o maior e o menor número da lista.

    :param numbers: lista de números.
    :type numbers: list
    :return: subtração entre o maior e o menor número da lista.
    :rtype: float | int
    """
    return max(numbers) - min(numbers)


def main():
    """Função principal."""
    print(large_difference([1, 2, 3]))
    print(large_difference([1, 3, 2]))
    print(large_difference([-2, 1, 3]))
    print(large_difference([-2, -1, -3]))
    print(large_difference([-2.5, -1, -3, -4.5]))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
