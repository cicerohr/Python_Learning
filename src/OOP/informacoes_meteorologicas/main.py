# -*- coding: utf-8 -*-
r"""main.py in: 2022-05-16."""

from InformacoesMeteorologicas import InformacoesMeteorologicas

from tests.loguru_conf import logger


def main():
    """Função principal."""
    cidade = input('Digite o nome da cidade: ').strip().title()
    info_meteorologica = InformacoesMeteorologicas(cidade)
    print(info_meteorologica)
    print(repr(info_meteorologica))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
