# -*- coding: utf-8 -*-
r"""feynman.py in: 2022-04-22.

Python version: 3.10.0

Quantos quadrados diferentes existem em um quadriculado de N x N quadrados?

Entrada
A entrada contém diversos casos de teste. Cada caso de teste é composto de uma
única linha, contendo apenas um inteiro N, representando o número de quadrados
em cada lado do quadriculado (1 ≤ N ≤ 100).
O final da entrada é indicado por uma linha contendo apenas um zero.

Saída
Para cada caso de teste na entrada, seu programa deve imprimir uma única linha,
contendo o número de diferentes quadrados para a entrada correspondente.
"""


def main():
    """Main function."""
    while True:
        n = int(input())
        if n == 0:
            break
        print(int(n * (n + 1) * (2 * n + 1) / 6))


if __name__ == '__main__':
    main()
