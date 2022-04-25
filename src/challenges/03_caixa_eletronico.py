# -*- coding: utf-8 -*-
r"""03_caixa_eletronico.py in: 2022-04-24.

Python version: 3.10.0

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário o valor do saque e depois informar quantas cédulas de cada valor serão
fornecidas. As cédulas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se
preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: para sacar a quantia de 256 reais, o programa fornece duas notas de
100, uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2: para sacar a quantia de 399 reais, o programa fornece três notas de
100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

https://pythonpro.com.br/desafio-python-em-14-dias-aula-3/

Testes:
    >>> CaixaEletronico().sacar(256)
    [100, 100, 50, 5, 1]
    >>> CaixaEletronico().sacar(399)
    [100, 100, 100, 50, 10, 10, 10, 10, 5, 1, 1, 1, 1]
    >>> CaixaEletronico().sacar(0)
    O valor mínimo para saque é de R$ 10.
    False
    >>> CaixaEletronico().sacar(601)
    O valor máximo para saque é de R$ 600.
    False
"""
from tests.loguru_conf import logger


class CaixaEletronico:
    """Classe para o caixa eletrônico."""

    def __init__(self):
        """Método construtor."""
        self.cedulas = [100, 50, 10, 5, 1]
        self.valor_minimo = 10
        self.valor_maximo = 600
        self.valor_saque = 0
        self.usuario_valor = 0
        self.notas_fornecidas = []

    def __str__(self) -> str:
        """Método para imprimir.

        :return: mensagem de saque
        :rtype: str
        """
        return f'Notas fornecidas: {self.notas_fornecidas}'

    def __repr__(self):
        """Representação do objeto.

        :return: representação do objeto.
        :rtype: str
        """
        return f'{type(self).__name__}.sacar({self.usuario_valor}) -> ' \
               f'{self.notas_fornecidas}'

    def sacar(self, saque: int) -> list | bool:
        """Método para sacar.

        :param saque: valor do saque.
        :return: notas fornecidas.
        :rtype: list | bool
        """
        self.valor_saque = self.usuario_valor = saque
        if self.valor_saque < self.valor_minimo:
            print(f'O valor mínimo para saque é de R$ {self.valor_minimo}.')
            logger.error(f'Valor mínimo é {self.valor_minimo}.')
            return False
        if self.valor_saque > self.valor_maximo:
            print(f'O valor máximo para saque é de R$ {self.valor_maximo}.')
            logger.error(f'Valor máximo é {self.valor_maximo}.')
            return False

        while self.valor_saque > 0:
            for cedula in self.cedulas:
                if self.valor_saque >= cedula:
                    self.valor_saque -= cedula
                    self.notas_fornecidas.append(cedula)
                    break
        return self.notas_fornecidas


def tratar_entrada(entrada: int | str) -> int | bool:
    """Tratar entrada do usuário.

    :param entrada: valor digitado.
    :return: valor do saque.
    :rtype: int | bool
    """
    try:
        valor_saque = int(entrada)
    except ValueError:
        logger.error(f'Valor inválido: {entrada}')
        print(f'"{entrada}" é inválido. Digite um valor inteiro.')
        return False
    return valor_saque


def main():
    """Função principal."""
    caixa = CaixaEletronico()
    while True:
        entrada = input('Digite o valor do saque: ')
        valor_saque = tratar_entrada(entrada)
        if not valor_saque:
            continue
        notas_fornecidas = caixa.sacar(valor_saque)
        if not notas_fornecidas:
            continue
        print(caixa)
        print(repr(caixa))
        break


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
