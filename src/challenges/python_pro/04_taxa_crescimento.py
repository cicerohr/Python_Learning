# -*- coding: utf-8 -*-
r"""04_taxa_crescimento.py in: 2022-04-24.

Python version: 3.10.0

Supondo que a população de um país A seja da ordem de 80 000 habitantes com uma
taxa anual de crescimento de 3% e que a população de B, seja 20 0000 habitantes
com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale
a população do país B, mantidas as taxas de crescimento.

https://pythonpro.com.br/desafio-python-em-14-dias-aula-4/

Testes:
    >>> TaxaCrescimento(80_000, 20_000)
    TaxaCrescimento(80000, 20000) -> 47008
    >>> TaxaCrescimento(20_000, 80_000)
    TaxaCrescimento(20000, 80000) -> 0
"""
from tests.loguru_conf import logger


class TaxaCrescimento:
    """Class TaxaCrescimento."""

    def __init__(self, pais_a: int, pais_b: int) -> None:
        """Método construtor.

        :param pais_a: population A
        :param pais_b: population B
        """
        self.pais_a = pais_a
        self.pais_b = pais_b
        self.taxa_a = 0.03
        self.taxa_b = 0.015

    def __str__(self) -> str:
        """Método str.

        :return: ‘string’ com os dados do objeto
        """
        return f'{self.calcular_anos()}'

    def __repr__(self) -> str:
        """Método que retorna uma ‘string’ representando o objeto.

        :return: ‘string’ representando o objeto
        """
        return (
            f'{type(self).__name__}({self.pais_a}, {self.pais_b}) -> '
            f'{self.calcular_anos()}'
        )

    def calcular_anos(self) -> int:
        """Calcula os anos necessários para igualar ou ultrapassar o país A.

        :return: anos necessários para igualar ou ultrapassar o país A
        :rtype: int
        """
        anos = 0
        while self.pais_a > self.pais_b:
            anos += 1
            self.pais_a += self.pais_a * self.taxa_a
            self.pais_b += self.pais_b * self.taxa_b
        return anos


def main():
    """Função principal."""
    print(TaxaCrescimento(80_000, 20_000))
    print(repr(TaxaCrescimento(80_000, 20_000)))
    logger.info(TaxaCrescimento(80_000, 20_000))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
