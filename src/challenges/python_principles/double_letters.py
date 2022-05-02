# -*- coding: utf-8 -*-
r"""double_letters.py in: 2022-05-01.

Python version: 3.10.0

O objetivo deste desafio é analisar uma ‘string’ para verificar se ela contém
duas letras iguais seguidas. Por exemplo, a ‘string’ "hello" tem l duas vezes
seguidas, enquanto a ‘string’ "nono" não tem duas letras idênticas seguidas.

Defina uma função chamada double_letters que recebe um único parâmetro.
O parâmetro é uma ‘string’. Sua função deve retornar True se houver duas letras
idênticas na ‘string’ ou False caso contrário.
"""
from tests.loguru_conf import logger


def double_letters(string: str) -> bool:
    """Função que verifica se há duas letras iguais seguidas.

    Explicação:

    * zip(): cria tuplas com os elementos das sequências de entrada.
    * list comprehension: lista com os elementos que satisfazem a condição.
    * any(): retorna True se verdadeiro para qualquer elemento da lista.

    zip(string, string[1:]) -> ('h', 'e'), ('e', 'l'), ('l', 'l'), ('l', 'o')

    [(a == b) -> True | False]

    any([False, False, True, False]) -> True

    for a, b in zip(string, string[1:]):
        if a == b:
            return True
    return False

    :param string: ‘string’ a ser analisada.
    :type string: str
    :return: True se duas letras iguais seguidas ou False caso contrário.
    :rtype: bool
    """
    return any([a == b for a, b in zip(string, string[1:])])


def main():
    """Função principal."""
    print(double_letters('hello'))
    print(double_letters('nono'))
    print(double_letters('ppoi'))
    print(double_letters('poii'))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
