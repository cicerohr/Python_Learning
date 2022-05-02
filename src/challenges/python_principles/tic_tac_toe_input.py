# -*- coding: utf-8 -*-
r"""tic_tac_toe_input.py in: 2022-05-01.

Python version: 3.10.0

Aqui está a história por trás deste desafio: imagine que você está escrevendo
um jogo da velha, onde o tabuleiro se parece com isso:

1:  X | O | X
    -----------
2:    |   |
    -----------
3:  O |   |
    A   B   C

O tabuleiro é representado como uma lista 2D:

placa = [
     ['X', 'O', 'X'],
     [' ', ' ', ' '],
     ['O', ' ', ' '],
]

Imagine se seu usuário digitar 'C1' e você precisar ver se há um X ou O nessa
célula do quadro. Para fazer isso, você precisa traduzir da ‘string’ 'C1' para
a linha 0 e coluna 2 para você poder verificar board[row][column].

Sua tarefa é escrever uma função que possa traduzir de ‘strings’
para uma tupla (linha, coluna). Nomeie sua função get_row_col; ele deve ter
um único parâmetro que é uma ‘string’ de coordenada consistindo de uma letra
maiúscula e um dígito.

Por exemplo, chamar get_row_col('A3') deve retornar a tupla (2, 0) porque A3
corresponde à linha no índice 2 e à coluna no índice 0 no quadro.

Referência:
https://en.wikipedia.org/wiki/List_of_Unicode_characters#Basic_Latin
"""
from tests.loguru_conf import logger


def get_row_col(string: str) -> tuple | str:
    """Traduz uma ‘string’ de coordenadas para uma tupla (linha, coluna).

    Ord() -> retorna inteiro correspondente ao caracter ‘Unicode’.

    :param string: string de coordenadas.
    :type string: str
    :return: tupla de coordenadas (linha, coluna) ou mensagem de erro.
    :rtype: tuple | str
    """
    string_upper = string.upper()
    row = int(string_upper[1]) - 1
    col = ord(string_upper[0]) - 65
    if row < 0 or row > 2 or col < 0 or col > 2:
        return f'{string} não é uma coordenada válida.'
    return row, col


def main():
    """Função principal."""
    print(get_row_col('A1'))
    print(get_row_col('b2'))
    print(get_row_col('C3'))
    print(get_row_col('D4'))
    print(get_row_col('a2'))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
