# -*- coding: utf-8 -*-
r"""utilitarios.py in: 2022-05-29.

@author: Cicero
"""
import time
from pathlib import Path

from tests.loguru_conf import logger


class Utilitarios:
    """Classe abstrata para utilitários."""

    def __init__(self):
        """Construtor da classe."""

    @staticmethod
    def caminho_relativo_assets() -> Path:
        """Retorna o caminho relativo à pasta assets."""
        return Path(__file__).parent / Path('assets')

    @staticmethod
    def gerar_nome_arquivo_qr_code() -> str:
        """Gera o nome do arquivo a partir da data e hora atual."""
        return f'qr_code_{time.strftime("%Y%m%d_%H%M%S")}.png'

    def __str__(self):
        """String do objeto."""

    def __repr__(self):
        """Representação do objeto."""
        return (
            f'<{self.__class__.__name__}> {self.__class__.__doc__}\n'
            f'{self.__class__.__module__} {self.__dict__}'
        )


def main():
    """Função principal."""
    print(Utilitarios.caminho_relativo_assets())
    print(Utilitarios.gerar_nome_arquivo_qr_code())


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
