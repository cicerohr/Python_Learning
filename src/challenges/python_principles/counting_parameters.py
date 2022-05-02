# -*- coding: utf-8 -*-
r"""counting_parameters.py in: 2022-05-02.

Python version: 3.10.0

Defina uma função param_count que receba um número variável de parâmetros.
A função deve retornar o número de argumentos com que foi chamada.

Por exemplo, param_count() deve retornar 0, enquanto param_count(2, 3, 4) deve
retornar 3.
"""
from tests.loguru_conf import logger


def param_count(*args):
    """Função para contar parâmetros.

    :param args: parâmetros
    :return: número de parâmetros
    :rtype: int
    """
    return len(args)


def main():
    """Função principal."""
    print(param_count())
    print(param_count(2, 3, 4))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
