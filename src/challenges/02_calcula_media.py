# -*- coding: utf-8 -*-
r"""02_calcula_media.py in: 2022-04-24.

Python version: 3.10.0

Faça um programa para a leitura de duas notas parciais de um aluno. O programa
deve calcular a média alcançada por aluno e apresentar:
    — A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    — A mensagem "Reprovado", caso a média for menor que sete;
    — A mensagem "Aprovado com Distinção", caso a média for igual a dez.

https://pythonpro.com.br/desafio-python-em-14-dias-aula-2/

Testes:
    >>> CalculaMedia(10, 10).calcular_media()
    10.0
    >>> CalculaMedia(0, 0).calcular_media()
    0.0
    >>> CalculaMedia(10, 2).calcular_media()
    6.0
    >>> CalculaMedia(10, '2').calcular_media()
    6.0
    >>> CalculaMedia(10, -1).calcular_media()
    Nota inválida: -1.0
    5.0
    >>> CalculaMedia('a', 'b').calcular_media()
    Nota inválida: a
    Nota inválida: b
    0.0
    >>> CalculaMedia(-1, 11).calcular_media()
    Nota inválida: -1.0
    Nota inválida: 11.0
    0.0
"""
from tests.loguru_conf import logger


class CalculaMedia:
    """Calcula a média de duas notas parciais."""

    def __init__(self, nota1: float | str = 0, nota2: float | str = 0):
        """Inicializa a classe.

        :param nota1: primeira nota do aluno.
        :param nota2: segunda nota do aluno.
        :default nota1: 0
        :default nota2: 0
        """
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0

    def __str__(self):
        """Retorna uma ‘string’ com a representação do objeto."""
        return f'{self.verificar_media()} - Média: {self.media}'

    def __repr__(self):
        """Retorna uma ‘string’ com a representação do objeto."""
        return f'{type(self).__name__}({self.nota1}, {self.nota2}) -> {self}'

    def ler_notas(self):
        """Lê as notas."""
        self.nota1 = input('Digite a primeira nota: ')
        self.nota2 = input('Digite a segunda nota: ')
        self.calcular_media()

    @staticmethod
    def transformar_nota(nota: float | str) -> float:
        """Transforma a nota para float."""
        try:
            nota = float(nota)
            if nota < 0 or nota > 10:
                raise ValueError
        except ValueError:
            print(f'Nota inválida: {nota}')
            logger.error(f'"{nota}" não é um número válido.')
            nota = 0
        return nota

    def calcular_media(self) -> float:
        """Calcula a média."""
        self.nota1 = self.transformar_nota(self.nota1)
        self.nota2 = self.transformar_nota(self.nota2)
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def verificar_media(self) -> str:
        """Verifica a média e retorna uma mensagem."""
        if self.media == 10:
            return 'Aprovado com Distinção'
        if self.media >= 7:
            return 'Aprovado'
        if self.media < 7:
            return 'Reprovado'
        logger.error(f'Média inválida: {self.media}')
        return f'Média inválida: {self.media}'


def main():
    """Função principal."""
    calcula_media = CalculaMedia()
    calcula_media.ler_notas()
    print(calcula_media)
    print('\n', repr(calcula_media))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
