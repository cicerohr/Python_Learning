# -*- coding: utf-8 -*-
r"""custom_zip.py in: 2022-05-01.

Python version: 3.10.0

A função zip embutida 'zipa' duas listas. Escreva sua própria implementação
desta função.

Defina uma função chamada zap. A função recebe dois parâmetros, a e b.
Isso são listas.

Sua função deve retornar uma lista de tuplas. Cada tupla deve conter um
elemento da lista a e um da lista b.

Você pode assumir que a e b têm comprimentos iguais.

Se você não entender, pense em um zíper.

Por exemplo:

zap(
     [0, 1, 2, 3],
     [5, 6, 7, 8]
)

Deve retornar:

[(0, 5),
  (1, 6),
  (2, 7),
  (3, 8)]
"""
from tests.loguru_conf import logger


def zap(a: list, b: list) -> list:
    """Função que faz a combinação de duas listas.

    :param a: lista 1.
    :type a: list
    :param b: lista 2.
    :type b: list
    :return: lista de tuplas com os elementos da lista 1 e 2.
    :rtype: list
    """
    return list(zip(a, b))


def main():
    """Função principal."""
    print(zap([0, 1, 2, 3], [5, 6, 7, 8]))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
