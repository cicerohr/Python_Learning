# -*- coding: utf-8 -*-
r"""Conversores.py in: 2022-05-17.

@author: Cícero
"""
from unicodedata import normalize

from tests.loguru_conf import logger


class Conversores:
    r"""Classe para conversões de dados.

    Conversor da direção do vento de graus para direção cardinal.

    Conversor de palavras acentuadas para palavras sem acentos.
    """

    @staticmethod
    def direcao_vento_cardinal(direcao_vento_graus: int) -> str:
        r"""Converte a direção do vento de graus para direção cardinal.

        :param direcao_vento_graus: direção do vento em graus.
        :type direcao_vento_graus: int.
        :return: direção do vento em direção cardinal.
        :rtype: str.
        """
        if 348.75 <= direcao_vento_graus <= 11.25:
            return 'Norte'
        if 11.25 <= direcao_vento_graus <= 33.75:
            return 'Nordeste'
        if 33.75 <= direcao_vento_graus <= 56.25:
            return 'Leste'
        if 56.25 <= direcao_vento_graus <= 78.75:
            return 'Sudeste'
        if 78.75 <= direcao_vento_graus <= 101.25:
            return 'Sul'
        if 101.25 <= direcao_vento_graus <= 123.75:
            return 'Sudoeste'
        if 123.75 <= direcao_vento_graus <= 146.25:
            return 'Oeste'
        if 146.25 <= direcao_vento_graus <= 168.75:
            return 'Noroeste'
        if 168.75 <= direcao_vento_graus <= 191.25:
            return 'Norte'
        if 191.25 <= direcao_vento_graus <= 213.75:
            return 'Nordeste'
        if 213.75 <= direcao_vento_graus <= 236.25:
            return 'Leste'
        if 236.25 <= direcao_vento_graus <= 258.75:
            return 'Sudeste'
        if 258.75 <= direcao_vento_graus <= 281.25:
            return 'Sul'
        if 281.25 <= direcao_vento_graus <= 303.75:
            return 'Sudoeste'
        if 303.75 <= direcao_vento_graus <= 326.25:
            return 'Oeste'
        if 326.25 <= direcao_vento_graus <= 348.75:
            return 'Noroeste'

    @staticmethod
    def palavra_acentuada_n_acentuada(palavra_acentuada: str) -> str:
        r"""Converte palavras acentuadas para palavras sem acentos.

        :param palavra_acentuada: palavra com acento.
        :type palavra_acentuada: str.
        :return: palavra sem acento.
        :rtype: str.
        """
        return (
            normalize('NFKD', palavra_acentuada)
            .encode('ASCII', 'ignore')
            .decode('ASCII')
        )

    def __repr__(self):
        return f'{self.__class__.__name__}()'


def main():
    """Função principal."""
    print(Conversores)
    print(Conversores.direcao_vento_cardinal(12))
    print(Conversores.palavra_acentuada_n_acentuada('Água'))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
