# -*- coding: utf-8 -*-
r"""05_calcula_soma_media.py in: 2022-04-24.

Python version: 3.10.0

Faça um programa que leia 5 números e informe a soma e a média dos números.

https://pythonpro.com.br/desafio-python-em-14-dias-aula-5/
"""
from tests.loguru_conf import logger


class CalculaSomaMedia:
    """Calcula a soma e a média dos números."""

    def __init__(self, n1: int, n2: int, n3: int, n4: int, n5: int) -> None:
        """Inicializa a classe.

        :param n1: número 1
        :param n2: número 2
        :param n3: número 3
        :param n4: número 4
        :param n5: número 5
        """
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5

    def __str__(self):
        """Retorna a string.

        :return: ‘string’ com a soma e a média dos números
        """
        return f'Soma: {self.soma()}\nMédia: {self.media()}'

    def __repr__(self):
        """Retorna a string representa a classe.

        :return: 'string' representa a classe
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.n1}, {self.n2}, {self.n3}, {self.n4}, {self.n5}'
            f') -> \n{self}'
        )

    def soma(self):
        """Retorna a soma dos números.

        :return: soma dos números
        """
        return self.n1 + self.n2 + self.n3 + self.n4 + self.n5

    def media(self):
        """Retorna a média dos números.

        :return: média dos números
        """
        return self.soma() / 5


def main():
    """Função principal."""
    print(CalculaSomaMedia(1, 2, 3, 4, 5))
    print(repr(CalculaSomaMedia(1, 2, 3, 4, 5)))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
