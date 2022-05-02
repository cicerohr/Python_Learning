# -*- coding: utf-8 -*-
r"""adding_removing_dots.py in: 2022-05-01.

Python version: 3.10.0

Escreva uma função chamada add_dots que recebe uma ‘string’ e adiciona '.'
entre cada letra.
Por exemplo, chamar add_dots("test") deve retornar a string 't.e.s.t'.

Em seguida, abaixo da função add_dots, escreva outra função chamada remove_dots
que remove todos os pontos de uma ‘string’.
Por exemplo, chamar remove_dots('t.e.s.t') deve retornar 'teste'.

Se ambas as funções estiverem corretas, chamar remove_dots(add_dots(string))
deve retornar a ‘string’ original para qualquer ‘string’.

(Você pode assumir que a entrada para add_dots não contém pontos.)
"""
from tests.loguru_conf import logger


def add_dots(string: str) -> str:
    """Adiciona pontos entre cada letra.

    :param string: string a ser adicionada pontos.
    :type string: str
    :return: string com pontos.
    :rtype: str
    """
    return '.'.join(string)


def remove_dots(string: str) -> str:
    """Remove pontos de uma ‘string’.

    :param string: string a ser removida pontos.
    :type string: str
    :return: string sem pontos.
    :rtype: str
    """
    return string.replace('.', '')


def main():
    """Função principal."""
    print(add_dots('test'))
    print(remove_dots('t.e.s.t'))
    print(remove_dots(add_dots('test')))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
