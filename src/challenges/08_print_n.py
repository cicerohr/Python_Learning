# -*- coding: utf-8 -*-
r"""08_print_n.py in: 2022-04-25.

Python version: 3.10.0

Faça um programa para imprimir:

1

1   2

1   2   3

1   2   3   ...  n

Para um "n" informado pelo usuário. Use uma função que receba um valor "n"
inteiro imprima até a n-ésima linha.
"""
from tests.loguru_conf import logger


class PrintN:
    r"""Classe PrintN."""

    def __init__(self, n: int) -> None:
        r"""Constructor da classe PrintN.

        :param n: número de linhas para imprimir.
        :type n: int
        :raises TypeError: se não for um inteiro.
        """
        if not isinstance(n, int):
            logger.error('"n" precisa ser um inteiro.')
            raise TypeError('"n" precisa ser um inteiro')
        self.n = n

    def print_n(self) -> None:
        r"""Método para imprimir até a n-ésima linha.

        :raises TypeError: se não for um inteiro.
        """
        if not isinstance(self.n, int):
            logger.error('"n" precisa ser um inteiro.')
            raise TypeError('"n" precisa ser um inteiro')
        for i in range(1, self.n + 1):
            print(i, end='')
            if i < self.n:
                print(' ', end='')
            if i % 10 == 0:
                print()


def main():
    r"""Main function."""
    n = int(input('Digite um número: '))
    imprimir = PrintN(n)
    imprimir.print_n()


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
