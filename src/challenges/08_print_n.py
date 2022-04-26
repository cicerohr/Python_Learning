# -*- coding: utf-8 -*-
r"""08_print_n.py in: 2022-04-25.

Python version: 3.10.0

Faça um programa para imprimir:

1

1   2

1   2   3

1   2   3   ...  n

Para um "numero" informado pelo usuário. Use uma função que receba um valor "n"
inteiro imprima até a n-ésima linha.
"""
from tests.loguru_conf import logger


class ImprimeNumeros:
    r"""Classe PrintN."""

    def __init__(self, numero: int) -> None:
        r"""Constructor da classe ImprimeNumeros.

        :param numero: número de linhas para imprimir.
        :type numero: int
        :raises TypeError: se não for um número inteiro.
        """
        if not isinstance(numero, int):
            logger.error('Precisa ser um número inteiro.')
            raise TypeError('Precisa ser um número inteiro.')
        self.numero = numero

    def imprimir_numeros(self) -> None:
        r"""Método para imprimir até o n-ésima número.

        :raises TypeError: se não for um número inteiro.
        """
        if not isinstance(self.numero, int):
            logger.error('Precisa ser um número inteiro.')
            raise TypeError('Precisa ser um número inteiro.')
        for i in range(1, self.numero + 1):
            print(i, end='')
            if i < self.numero:
                print(' ', end='')
            if i % 10 == 0:
                print()


def main():
    r"""Main function."""
    n = int(input('Digite um número: '))
    imprimir = ImprimeNumeros(n)
    imprimir.imprimir_numeros()


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
