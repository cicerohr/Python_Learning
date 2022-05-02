# -*- coding: utf-8 -*-
r"""anagrams.py in: 2022-05-01.

Python version: 3.10.0

Duas ‘strings’ são anagramas se você puder fazer uma partir da outra
reorganizando as letras.

Escreva uma função chamada is_anagram que receba duas ‘strings’ como seus
parâmetros. Sua função deve retornar True se as ‘strings’ forem anagramas e
False caso contrário.

Por exemplo, a chamada is_anagram('typhoon', 'opython') deve retornar True
enquanto a chamada is_anagram('Alice', 'Bob') deve retornar False.
"""
from tests.loguru_conf import logger


def is_anagram(word1: str, word2: str) -> bool:
    """Verifica se duas palavras são anagramas.

    :param word1: primeira palavra.
    :type word1: str
    :param word2: segunda palavra.
    :type word2: str
    :return: True se as palavras forem anagramas. False caso contrário.
    :rtype: bool
    """
    return sorted(word1) == sorted(word2)


def main():
    """Função principal."""
    print(is_anagram('typhoon', 'opython'))
    print(is_anagram('Alice', 'Bob'))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
