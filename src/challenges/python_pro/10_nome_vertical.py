# -*- coding: utf-8 -*-
r"""10_nome_vertical.py in: 2022-04-26.

Python version: 3.10.0

Nome na vertical em escada invertida. Altere o programa anterior de modo que a
escada seja invertida.
"""
from tests.loguru_conf import logger


class NomeVertical:
    """Classe NomeVertical.

    Imprime o nome na vertical diminuindo a última letra por linha.
    """

    def __init__(self, nome: str) -> None:
        """Construtor da classe.

        :param nome: nome a ser impresso na vertical.
        :type nome: str
        """
        self.nome = nome

    def __str__(self) -> str:
        """Retorna a string do objeto.

        :return: string do objeto.
        :rtype: str
        """
        return f'{self.__class__.__name__}({self.__dict__})'

    def __repr__(self) -> str:
        """Representação da classe.

        :return: representação da classe.
        :rtype: str
        """
        return (
            f'<class {self.__class__.__name__}> {self.__class__.__doc__}'
            f'\n{self.__class__.__module__} {self.__dict__}'
        )

    def imprimir(self) -> None:
        """Imprime o nome na vertical."""
        for indice, _ in enumerate(self.nome, start=1):
            if indice == 1:
                print(self.nome)
            print(self.nome[:-indice])


def main():
    """Função principal."""
    nome = input('Digite seu nome: ')
    nome_vertical = NomeVertical(nome)
    nome_vertical.imprimir()
    print(nome_vertical)
    print(repr(nome_vertical))
    logger.info('Nome impresso na vertical.')


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
