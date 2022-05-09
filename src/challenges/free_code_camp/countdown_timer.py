# -*- coding: utf-8 -*-
r"""countdown_timer.py in: 2022-05-05.

Python version: 3.10.0
"""
from time import sleep

from tests.loguru_conf import logger


class ContadorRegressivo:
    r"""Contador regressivo.

    Esta classe conta, regressivamente, o tempo em segundos.

    O usuário define o tempo em segundos e o contador inicia a contagem
    regressiva.
    """

    def __init__(self, tempo: int) -> None:
        """Método construtor.

        :param tempo: tempo em segundos.
        :type tempo: int
        """
        self.tempo_inicial = tempo
        self.tempo = tempo
        self.temporizador = ''

    def contagem_regressiva(self):
        """Contagem regressiva.

        Conta regressivamente o tempo em segundos.
        """
        while self.tempo > 0:
            # divmod() retorna um tupla com o resultado da divisão inteira
            # e o resto.
            # divmod(a, b) -> (a // b, a % b)
            minutos, segundos = divmod(self.tempo, 60)
            self.temporizador = f'{minutos:02d}:{segundos:02d}'
            self.__str__()
            sleep(1)
            self.tempo -= 1

        print(
            '\n',
            f'Fim da contagem regressiva de {self.tempo_inicial} s!',
            end='\n\n',
        )

    def __str__(self) -> object:
        """Retorna a contagem do tempo no formato 00:00."""
        return print('\r', self.temporizador, end='')

    def __repr__(self) -> str:
        """Representação do objeto."""
        return (
            f'<{self.__class__.__name__}> {self.__class__.__doc__}\n'
            f'{self.__class__.__module__} {self.__dict__}'
        )


def main():
    """Função principal."""
    contador = ContadorRegressivo(tempo=65)
    contador.contagem_regressiva()
    print(repr(contador))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
