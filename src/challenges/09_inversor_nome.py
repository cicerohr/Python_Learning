# -*- coding: utf-8 -*-
r"""09_inversor_nome.py in: 2022-04-26.

Python version: 3.10.0

Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário
digitar o seu nome e em seguida mostre o nome do usuário detrás para frente
utilizando somente letras maiúsculas.

Dica: lembre−se que ao informar o nome o usuário pode digitar letras
maiúsculas ou minúsculas.

https://pythonpro.com.br/desafio-python-em-14-dias-aula-9/

Teste:
    >>> nome = 'Luiz Otávio'
    >>> inverte = InverteNome(nome)
    >>> inverte.inverter_nome()
    'OIVÁTO ZIUL'
"""
from tests.loguru_conf import logger


class InverteNome:
    """Classe para inverter nome."""

    def __init__(self, nome: str) -> None:
        """Método construtor.

        :param nome: nome a ser invertido.
        :type nome: str
        """
        self.nome = nome
        self.nome_invertido = ''

    def __str__(self) -> str:
        """Retorna o nome invertido.

        :return: nome invertido.
        :rtype: str
        """
        return self.nome_invertido

    def __repr__(self) -> str:
        """Representação da classe.

        :return: representação da classe.
        :rtype: str
        """
        return (
            f'<class {self.__class__.__name__}> {self.__class__.__doc__}'
            f'\n{self.__class__.__module__} {self.__dict__}'
        )

    def inverter_nome(self) -> str:
        """Inverte o nome e coloca em letras maiúsculas.

        :return: nome invertido.
        :rtype: str
        """
        self.nome_invertido = self.nome[::-1].upper()
        return self.nome_invertido


def main():
    """Programa principal."""
    nome = input('Digite seu nome: ')
    inverte = InverteNome(nome)
    inverte.inverter_nome()
    print(inverte)
    print(repr(inverte))
    logger.info(f'Nome invertido: {inverte}')


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
