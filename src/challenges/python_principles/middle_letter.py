# -*- coding: utf-8 -*-
r"""middle_letter.py in: 2022-04-30.

Python version: 3.10.0


"""
from tests.loguru_conf import logger


def mid(word: str) -> str:
    """Retorna a letra central de una palavra.

    A função deve extrair e devolver a letra do meio. Se não houver uma letra
    do meio, sua função deve retornar a sequência vazia.

    Por exemplo, mid ("abc") deve retornar "b" e mid ("aaaa") deve retornar.

    :param word: palavra ou frase a ser analisada.
    :type word: str
    :return: ‘string’ com a letra do meio, ou vazio se não houver.
    :rtype: str
    """
    return word[len(word) // 2] if len(word) % 2 != 0 else ''


def main():
    print(mid('abc'))
    print(mid('Python'))
    print(mid('Python is a programming language!'))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
