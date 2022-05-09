# -*- coding: utf-8 -*-
r"""hangman.py in: 2022-05-03.

Python version: 3.10.0
"""
import json
from random import choice

from tests.loguru_conf import logger


class JogoDaForca:
    """Classe para jogar o Jogo da Forca.

    O jogo da forca é um jogo de adivinhação de palavras.

    Inicialmente, a classe deverá escolher uma palavra secreta, no arquivo
    palavras.json, que será usada para o jogo. O formato do arquivo é:
    {
      "alfinete": {
        "nome": "alfinete",
        "sem acentos": "alfinete",
        "dica": "Usado em costuras"
      },
    }

    A classe apresenta um tabuleiro do jogo da forca, sendo que a cada erro
    uma parte do corpo é mostrada na forca.

    A palavra secreta é ocultada com '_' para cada letra. Quando o usuário
    acerta a letra, a letra substitui o '_' na palavra secreta.

    O jogo termina quando o usuário acertar a palavra ou quando o usuário
    errar 6 vezes.
    """

    def __init__(self):
        """Inicializa o jogo da forca."""
        self.tupla_palavra = self.escolher_palavra()
        self.palavra_secreta = self.tupla_palavra[0]
        self.palavra_secreta_sem_acentos = self.tupla_palavra[1]
        self.palavra_secreta_oculta = self.ocultar_palavra()
        self.dica = self.tupla_palavra[2]
        self.letra = ''
        self.letras_acertadas = []
        self.letras_erradas = []
        self.erros = 0
        self.acertos = 0
        self.tabuleiro = [
            '  _________',
            ' |/        |',
            ' |          ',
            ' |          ',
            ' |          ',
            ' |          ',
            '_|_________ ',
        ]

    @staticmethod
    def escolher_palavra() -> tuple:
        """Escolhe uma palavra secreta."""
        with open('palavras.json', 'r', encoding='utf-8') as arquivo:
            palavras = json.load(arquivo)
        palavra_escolhida = choice(list(palavras.keys()))
        return (
            palavras[palavra_escolhida]['nome'],
            palavras[palavra_escolhida]['sem acentos'],
            palavras[palavra_escolhida]['dica'],
        )

    def ocultar_palavra(self) -> str:
        """Oculta a palavra secreta."""
        return '_' * len(self.palavra_secreta)

    def mostrar_palavra_secreta_oculta(self):
        """Mostra a palavra secreta oculta."""
        print(' '.join(self.palavra_secreta_oculta))

    def controlar_palavra_secreta_oculta(self) -> str:
        """Controle da palavra secreta oculta.

        A cada acerto, o '_' é substituido pela letra acertada em sua posição
        na palavra secreta original.
        """
        if self.letras_acertadas:
            for i, letra in enumerate(self.palavra_secreta_sem_acentos):
                if self.letra == letra:
                    self.palavra_secreta_oculta = (
                        # mostra os caracteres até o índice da letra -1
                        self.palavra_secreta_oculta[:i]
                        + self.letra
                        # mostra os caracteres a partir do índice da letra +1
                        + self.palavra_secreta_oculta[i + 1:]
                    )
        return self.palavra_secreta_oculta

    def mostrar_dica(self):
        """Mostra a dica da palavra secreta."""
        print('-' * 50)
        print(f'Dica: {self.dica}.')
        print('-' * 50)

    def mostrar_tabuleiro(self):
        """Controle do tabuleiro.

        A cada erro, uma parte do corpo é mostrada na forca.
        """
        match self.erros:
            case 1:
                self.tabuleiro[2] = ' |         \U0001F62E'  # cabeca
            case 2:
                self.tabuleiro[2] = ' |         \U0001F61F'  # cabeca
                self.tabuleiro[3] = ' |         |'  # torso
            case 3:
                self.tabuleiro[2] = ' |         \U0001F641'  # cabeca
                self.tabuleiro[3] = ' |        /|'  # torso e braço esquerdo
            case 4:
                self.tabuleiro[2] = ' |         \U0001F625'  # cabeca
                self.tabuleiro[
                    3
                ] = ' |        /|\\'  # torso, braço esquerdo e direito
            case 5:
                self.tabuleiro[2] = ' |         \U0001F62D'  # cabeca
                self.tabuleiro[
                    3
                ] = ' |        /|\\'  # torso, braço esquerdo e direito
                self.tabuleiro[4] = ' |        /'  # perna esquerda
                self.mostrar_dica()
            case 6:
                self.tabuleiro[2] = ' |         \U0001F61E'  # cabeca
                self.tabuleiro[
                    3
                ] = ' |        /|\\'  # torso, braço esquerdo e direito
                self.tabuleiro[
                    4
                ] = ' |        / \\'  # perna esquerda e direita
        print('\n'.join(self.tabuleiro))

    def escolher_letra(self):
        """Controle da letra escolhida pelo usuário.

        Verifica se a letra escolhida pelo usuário já foi utilizada.

        Verifica se a letra escolhida pelo usuário está na palavra secreta.
        """
        self.letra = input('Digite uma letra: ')[0].strip().lower()
        if (
            self.letra in self.letras_acertadas
            or self.letra in self.letras_erradas
        ):
            print('Você já escolheu essa letra!')
            self.escolher_letra()
        elif self.letra in self.palavra_secreta_sem_acentos:
            self.letras_acertadas.append(self.letra)
            self.acertos += 1
            self.controlar_palavra_secreta_oculta()
        else:
            self.letras_erradas.append(self.letra)
            self.erros += 1

    def jogar(self):
        """Inicia o jogo.

        Verifica se o usuário ganhou ou perdeu.
        """
        print(
            '-' * 50,
            'Bem-vindo ao Jogo Da Forca!'.center(50),
            '-' * 50,
            sep='\n',
        )
        while True:
            self.mostrar_tabuleiro()
            self.mostrar_palavra_secreta_oculta()
            self.escolher_letra()
            if self.palavra_secreta_oculta == self.palavra_secreta_sem_acentos:
                mensagem_fim = 'Parabéns, você acertou!'
                break
            if self.erros == 6:
                mensagem_fim = 'Você perdeu!'
                break

        self.mostrar_tabuleiro()
        print(f'\n{mensagem_fim}', end='\n\n')
        self.mostrar_dados()
        self.jogar_novamente()

    def jogar_novamente(self):
        """Pergunta se o usuário quer jogar novamente.

        Se o usuário digitar 's', o jogo inicia novamente.
        """
        pergunta = input('Deseja jogar novamente? (s/n): ').strip().lower()
        if pergunta != 's':
            print('\n', 'Obrigado por jogar!', end='\n\n')
            exit()
        self.__init__()
        self.jogar()

    def mostrar_dados(self):
        """Imprime para o usuário os dados do jogo."""
        print(self.__str__())

    def __str__(self) -> str:
        """Retorna uma ‘string’ com os dados do jogo."""
        return (
            f'Palavra secreta: {self.palavra_secreta}\n'
            f'Dica: {self.dica}\n'
            f'Letras acertadas: {self.letras_acertadas}\n'
            f'Letras erradas: {self.letras_erradas}\n'
            f'Erros: {self.erros}\n'
            f'Acertos: {self.acertos}\n'
        )

    def __repr__(self) -> str:
        """Representação do objeto."""
        return (
            f'<{self.__class__.__name__}> {self.__class__.__doc__}\n'
            f'{self.__class__.__module__} {self.__dict__}'
        )


def main():
    """Função principal."""
    jogo = JogoDaForca()
    jogo.jogar()
    print(repr(jogo))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
