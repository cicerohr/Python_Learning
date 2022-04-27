# -*- coding: utf-8 -*-
r"""07_busca_salarios.py in: 2022-04-25.

Python version: 3.10.0

Utilize uma lista para resolver o problema a seguir. Uma empresa paga a seus
vendedores com base em comissões. O vendedor recebe R$ 200 por semana mais
9 % de suas vendas brutas daquela semana.

Por exemplo, um vendedor que teve vendas brutas de R$ 3_000 em uma semana
recebe R$ 200 mais 9 % de R$ 3_000, ou seja, um total de R$ 470.
Escreva um programa (usando um array de contadores) que determine quantos
vendedores receberam salários nos seguintes intervalos de valores:

. A R$ 200 - R$ 299;

. B R$ 300 - R$ 399;

. C R$ 400 - R$ 499;

. D R$ 500 - R$ 599;

. E R$ 600 - R$ 699;

. F R$ 700 - R$ 799;

. G R$ 800 - R$ 899;

. H R$ 900 - R$ 999;

. I R$ 1_000 em diante.

https://pythonpro.com.br/desafio-python-em-14-dias-aula-7/
"""
from tests.loguru_conf import logger


class ContagemFaixaSalarial:
    """Classe para contagem de faixa salarial."""

    def __init__(self, salarios: list) -> None:
        """Inicializa a classe.

        :param salarios: lista com os salários.
        """
        self.salarios = salarios
        self.contagem_faixa_salarial = [0] * 9

    def __str__(self) -> str:
        """Retorna a ‘string’ formatada.

        :return: ‘string’ formatada com os valores da lista.
        :rtype: str
        """
        return str(self.contagem_faixa_salarial)

    def __repr__(self):
        """Representação da classe.

        :return: representação da classe.
        :rtype: str
        """
        return (
            f'<class {self.__class__.__name__}> {self.__class__.__doc__}'
            f'\n{self.__class__.__module__} {self.__dict__}'
        )

    def contar_faixa_salarial(self) -> list:
        """Método para contar a faixa salarial.

        :return: lista com a contagem de cada faixa salarial.
        :rtype: list
        """
        for salario in self.salarios:
            indice = salario // 100 - 2
            indice_maximo = len(self.contagem_faixa_salarial) - 1
            indice = min(indice, indice_maximo)
            self.contagem_faixa_salarial[indice] += 1
            logger.debug(f'{salario} -> {indice}')
        return self.contagem_faixa_salarial


def main():
    """Função de chamada da classe."""
    salarios = [200, 300, 350, 500, 600, 630, 900, 901, 1000, 1100, 1200, 1300]
    contar = ContagemFaixaSalarial(salarios)
    print(contar.contar_faixa_salarial())
    print('\n', repr(contar))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
