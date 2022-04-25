# -*- coding: utf-8 -*-
r"""06_inverte_vetor.py in: 2022-04-25.

Python version: 3.10.0

Faça um Programa que leia um vetor de 10 números reais e mostre-os
na ordem inversa.

https://pythonpro.com.br/desafio-python-em-14-dias-aula-6/
"""
from tests.loguru_conf import logger


class InverteVetor:
    """Class InverteVetor."""

    def __init__(self):
        """Método construtor."""
        self.vetor_entrada = []
        self.vetor = []

    def __str__(self) -> str:
        """String do objeto.

        :return: string
        :rtype: str
        """
        return f'{self.vetor}'

    def __repr__(self) -> str:
        """Representação do objeto.

        :return: ‘string’ representando o objeto.
        :rtype: str
        """
        return (
            f'{self.__class__.__name__}({self.vetor_entrada}) '
            f'-> {self.vetor}'
        )

    def ler_vetor(self):
        """Ler vetor."""
        for i in range(10):
            self.vetor.append(int(input(f'Digite o {i + 1}º número: ')))

        self.vetor_entrada = self.vetor.copy()

    def inverter_vetor(self):
        """Inverte vetor."""
        self.vetor.reverse()


def main():
    """Função main."""
    inv = InverteVetor()
    inv.ler_vetor()
    inv.inverter_vetor()
    print(inv)
    print(repr(inv))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
