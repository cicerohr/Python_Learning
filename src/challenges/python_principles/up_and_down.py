# -*- coding: utf-8 -*-
r"""up_and_down.py in: 2022-05-01.

Python version: 3.10.0

Defina uma função chamada up_down que receba um único número como parâmetro.
Sua função retorna uma tupla contendo dois números; o primeiro deve ser um
inferior ao parâmetro, e o segundo deve ser um superior.

Por exemplo, chamar up_down(5) deve retornar (4, 6).
"""
from tests.loguru_conf import logger


def up_down(number: int) -> tuple:
    """Retorna um tupla com dois números.

    O primeiro é um número inferior ao parâmetro, e o segundo é
    um número superior.

    :param number: número a ser analisado.
    :type number: int
    :return: tupla com dois números.
    :rtype: tuple
    """
    return number - 1, number + 1


def main():
    """Função principal."""
    print(up_down(5))
    print(up_down(10))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
