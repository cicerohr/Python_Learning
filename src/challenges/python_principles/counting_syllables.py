# -*- coding: utf-8 -*-
r"""counting_syllables.py in: 2022-05-01.

Python version: 3.10.0

Defina uma função chamada count que recebe um único parâmetro. O parâmetro é
uma ‘string’. A ‘string’ conterá uma única palavra dividida em sílabas por
hífens, como estes:

'ho-tel'
'cat'
'met-a-phor'
'ter-min-a-tor'

Sua função deve contar o número de sílabas e devolvê-lo.

Por exemplo, a contagem de chamadas('ho-tel') deve retornar 2.
"""
from tests.loguru_conf import logger


def count(word):
    """Função que conta o número de sílabas."""
    return len(word.split('-'))


def main():
    """Função principal."""
    words = ['ho-tel', 'cat', 'met-a-phor', 'ter-min-a-tor']
    for word in words:
        print(
            f'{word} tem {count(word)} sílaba{"s" if count(word) > 1 else ""}.'
        )


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
