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

    def __init__(self) -> None:
        r"""Construtor da classe.

        Inicialização das direções do vento.

        :return: None.
        """
        self.direcoes = {
            'N (norte)': (348.75, 11.25),
            'NNE (nor-nordeste)': (11.26, 33.75),
            'NE (nordeste)': (33.76, 56.25),
            'ENE (leste–nordeste)': (56.26, 78.75),
            'E (leste)': (78.76, 101.25),
            'ESE (leste–sudeste)': (101.26, 123.75),
            'SE (sudeste)': (123.76, 146.25),
            'SSE (sul-sudeste)': (146.26, 168.75),
            'S (sul)': (168.76, 191.25),
            'SSO (sul-sudoeste)': (191.26, 213.75),
            'SO (sudoeste)': (213.76, 236.25),
            'OSO (oeste–sudoeste)': (236.26, 258.75),
            'O (oeste)': (258.76, 281.25),
            'ONO (oeste–noroeste)': (281.26, 303.75),
            'NO (noroeste)': (303.76, 326.25),
            'NNO (nor-noroeste)': (326.26, 348.74),
        }

    def direcao_cardinal(self, graus) -> str:
        """Converte graus para direção cardinal.

        :param graus: direção do vento em graus.
        :type graus: float.
        :return: direção do vento de forma cardinal.
        :rtype: str.
        """
        for chave, (inferior, superior) in self.direcoes.items():
            if 0 <= graus <= 11.25 or 348.75 <= graus < 360:
                return 'N (norte)'
            if inferior <= graus <= superior:
                return chave

    @staticmethod
    def retirar_acento(palavra_acentuada: str) -> str:
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

    def __repr__(self) -> str:
        r"""Representação do objeto.

        :return: representação do objeto.
        :rtype: str.
        """
        return f'{self.__class__.__name__}()'


def main():
    """Função principal."""
    conversores = Conversores()
    graus = 0.0
    while 0 <= graus < 360:
        print(f'{graus:.2f}°: {conversores.direcao_cardinal(graus)}')
        graus += 11.25
    print(conversores.retirar_acento('Água'))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
