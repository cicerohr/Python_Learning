# -*- coding: utf-8 -*-
r"""01_loja_tintas.py in: 2022-04-23.

Python version: 3.10.0

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os
respectivos preços em 3 situações:
    — Comprar apenas latas de 18 litros;
    — Comprar apenas galões de 3,6 litros;
    — Misturar latas e galões, de forma que o desperdício de tinta seja menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
    considere latas cheias.

https://pythonpro.com.br/desafio-python-em-14-dias-aula-1/
"""

from tests.loguru_conf import logger

setup = {'preco_lata': 80.00, 'preco_galao': 25.00, 'folga': 10}


class LojaTintas:
    """Loja de tintas."""

    def __init__(
            self,
            area: float,
            preco_lata: float = setup['preco_lata'],
            preco_galao: float = setup['preco_galao'],
            folga: float = setup['folga'],
    ) -> None:
        """Inicialização do objeto.

        :param area: area a ser pintada.
        :param preco_lata: preço da lata de tinta.
        :param preco_galao: preço do galão de tinta.
        :param folga: porcentagem de folga.
        """
        self.area = area
        self.total_tinta = (area / 6) * ((folga / 100) + 1)
        self.total_latas = round(self.total_tinta / 18 + 0.5)
        self.total_galoes = round(self.total_tinta / 3.6 + 0.5)
        self.preco_lata = preco_lata
        self.preco_galao = preco_galao
        self.folga = folga

    def __str__(self) -> str:
        """Retorna uma ‘string’ com os valores calculados.

        :return: ‘string’ com os valores calculados.
        """
        return (
            f'==========================================================\n\n'
            f'Para pintar {self.area} m², você precisará de:\n'
            f'{self.total_tinta:.2f} l ({self.folga} % de folga)\n'
            f'\n--------------- Somente Latas de 18 litros --------------\n'
            f'Total de latas: {self.total_latas}\n'
            f'Preço total: R$ {self.total_latas * self.preco_lata:.2f}\n'
            f'\n--------------- Somente Galões de 3,6 litros ------------\n'
            f'Total de galões: {self.total_galoes}\n'
            f'Preço total: R$ {self.total_galoes * self.preco_galao:.2f}\n'
            f'\n--------------- Latas e Galões --------------------------\n'
            f'Total de latas: {self.calcula_latas_galoes()[0]}\n'
            f'Total de galões: {self.calcula_latas_galoes()[1]}\n'
            f'Preço total de latas: R$ {self.preco_total_latas():.2f}\n'
            f'Preço total de galões: R$ {self.preco_total_galoes():.2f}\n'
            f'Preço total: R$ {self.preco_total():.2f}\n'
            f'Tinta desperdicada: {self.calcula_tinta_desperdicada():.2f} l '
            f'({self.calcula_tinta_desperdicada_porcentagem():.2f} %)\n'
        )

    def __repr__(self) -> str:
        """Retorna uma 'string' com a representação do objeto.

        :return: representação do objeto.
        """
        return f'{type(self).__name__}' \
               f'({self.area}, ' \
               f'{self.preco_lata}, ' \
               f'{self.preco_galao}, ' \
               f'{self.folga})'

    def calcula_latas_galoes(self) -> tuple:
        """Calcula o número de latas e galões.

        :return: tupla com o número de latas e galões.
        """
        if self.total_tinta % 18 != 0:
            total_latas = int(self.total_tinta // 18)
            total_galoes = round(self.total_tinta % 18 / 3.6 + 0.5)
        else:
            total_latas = round(self.total_tinta // 18 + 0.5)
            total_galoes = 0

        return total_latas, total_galoes

    def preco_total_latas(self) -> float:
        """Calcula o preço total de latas.

        :return: preço total das latas.
        """
        return self.preco_lata * self.calcula_latas_galoes()[0]

    def preco_total_galoes(self) -> float:
        """Calcula o preço total de galões.

        :return: preço total dos galões.
        """
        return self.preco_galao * self.calcula_latas_galoes()[1]

    def preco_total(self) -> float:
        """Calcula o preço total.

        :return: preço total.
        """
        return self.preco_total_latas() + self.preco_total_galoes()

    def calcula_tinta_desperdicada(self) -> float:
        """Calcula o tinta desperdicada.

        :return: tinta desperdicada.
        """
        return (
                       self.calcula_latas_galoes()[0] * 18
                       + self.calcula_latas_galoes()[1] * 3.6
               ) - self.total_tinta

    def calcula_tinta_desperdicada_porcentagem(self) -> float:
        """Calcula a tinta desperdicada em porcentagem.

        :return: tinta desperdicada em porcentagem.
        """
        return (self.calcula_tinta_desperdicada() / self.total_tinta) * 100


def so_numero(numero: float | str) -> bool:
    """Verifica se o valor é um float e nao uma ‘string’.

    :param numero: valor a ser verificado.
    :return: True se for um float. False caso contrário.
    """
    try:
        float(numero)
        return True
    except ValueError:
        return False


def main():
    """Programa de chamada da classe."""
    area = 0
    while True:
        try:
            area = float(input('Digite a área a ser pintada (m²): '))
            if so_numero(area) and area > 0:
                break
            print(f'Valor inválido: {area}! Tente novamente.', end='\n\n')
        except ValueError:
            print('Valor inválido! Tente novamente.', end='\n\n')
            logger.error(f'Valor inválido: {area}!')
            continue

    print()
    logger.info(repr(LojaTintas(area)))
    print(LojaTintas(area))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
