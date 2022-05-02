# -*- coding: utf-8 -*-
r"""palindrome.py in: 2022-05-01.

Python version: 3.10.0

Uma ‘string’ é um palíndromo quando é a mesma quando lida de trás para frente.

Por exemplo, a ‘string’ 'bob' é um palíndromo. Assim é 'abba'. Mas a ‘string’
'abcd' não é um palíndromo, porque 'abcd' != 'dcba'.

Escreva uma função chamada palindrome que receba uma única ‘string’ como
parâmetro. Sua função deve retornar True se a ‘string’ for um palíndromo e
False caso contrário.
"""
from tests.loguru_conf import logger


def palindrome(string: str) -> bool:
    """Verifica se a ‘string’ é um palíndromo.

    :param string: string a ser verificada.
    :type string: str
    :return: True se for um palíndromo e False caso contrário.
    :rtype: bool
    """
    return string == string[::-1]


def main():
    """Função principal."""
    print(palindrome('bob'))
    print(palindrome('abba'))
    print(palindrome('abcd'))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
