# -*- coding: utf-8 -*-
r"""all_equal.py in: 2022-05-01.

Python version: 3.10.0

Defina uma função chamada all_equal que receba uma lista e verifique se todos
os elementos da lista são iguais.

Por exemplo, chamar all_equal([1, 1, 1]) deve retornar True.
"""
from tests.loguru_conf import logger


def all_equal(lista):
    """Verifica se todos os elementos da lista são iguais."""
    return all(lista[0] == x for x in lista)


def main():
    """Função principal."""
    print(all_equal([1, 1, 1]))
    print(all_equal([1, 2, 3]))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
