# -*- coding: utf-8 -*-
r"""rock_paper_scissors.py in: 2022-05-03.

Python version: 3.10.0
"""
from random import randint

from tests.loguru_conf import logger


class JogoPedraPapelTesoura:
    """Classe para o jogo 'Pedra Papel e Tesoura'.

    A classe solicita o nome do usuário.

    O usuário escolhe uma entre 3 opções ('pedra', 'papel' e 'tesoura') e a
    classe faz uma escolha aleatória.
    """

    def __init__(self):
        """Inicializa o jogo."""
        self.opcoes = {1: 'pedra', 2: 'papel', 3: 'tesoura'}
        self.nome_usuario = input('Digite seu nome: ')
        self.escolha_usuario = None
        self.escolha_computador = None
        self.resultado = None

    def escolher_computador(self):
        """Método que escolhe uma opção aleatória para o computador."""
        self.escolha_computador = self.opcoes[randint(1, 3)]

    def escolher_usuario(self):
        """Método onde o usuário escolhe uma opção."""
        for key, value in self.opcoes.items():
            print(f'{key} - {value}')
        print()
        while True:
            try:
                self.escolha_usuario = self.opcoes[int(input('Escolha: '))]
                break
            except KeyError:
                print(f'Opção inválida! {self.opcoes}')
            except ValueError:
                print('Digite um número entre 1 e 3!')
                continue

    def obter_resultado(self):
        """Método que verifica o resultado do jogo.

        Lógica: pedra > tesoura > papel > pedra
        """
        match_ = {
            'pedra': {
                'pedra': 'Empate!',
                'papel': 'Você perdeu!',
                'tesoura': 'Você ganhou!',
            },
            'papel': {
                'pedra': 'Você ganhou!',
                'papel': 'Empate!',
                'tesoura': 'Você perdeu!',
            },
            'tesoura': {
                'pedra': 'Você perdeu!',
                'papel': 'Você ganhou!',
                'tesoura': 'Empate!',
            },
        }
        self.resultado = match_[self.escolha_usuario][self.escolha_computador]

    def jogar(self):
        """Método para inicia o jogo."""
        self.escolher_computador()
        self.escolher_usuario()
        self.obter_resultado()

    def __str__(self):
        """Retorna uma ‘string’ com o resultado do jogo."""
        return (
            f'{self.nome_usuario}, você escolheu {self.escolha_usuario} e '
            f'o computador escolheu {self.escolha_computador}. '
            f'{self.resultado}'
        )

    def __repr__(self) -> str:
        """Representação do objeto."""
        return (
            f'<{self.__class__.__name__}> {self.__class__.__doc__}\n'
            f'{self.__class__.__module__} {self.__dict__}'
        )


def main():
    """Função principal."""
    jogo = JogoPedraPapelTesoura()
    jogo.jogar()
    print(jogo, end='\n\n')
    # print(repr(jogo))


if __name__ == '__main__':
    logger.info('Início do programa')
    main()
    logger.info('Fim do programa')
