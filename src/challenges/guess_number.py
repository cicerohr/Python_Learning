# -*- coding: utf-8 -*-
r"""guess_number.py in: 2022-04-08.

Python version: 3.10.0

O programa deve:
    -Exibir uma mensagem de boas-vindas
    -Fornecer a possibilidade do usuário sair do jogo digitando 's'
    -Lidar com a entrada do usuário corretamente:
        -Esperamos receber um número inteiro entre 1 e 100
    -Verificar se o palpite esta correto e, caso não, informar se o palpite é
    maior ou menor que o número secreto
    -Informar quantas tentativas o programa leva para acertar o número secreto
    -Perguntar deseja jogar novamente ou sair, após acertar o número secreto
    -Exibir uma mensagem de jogo novo ou sair, conforme a resposta do usuário
    -Exibir uma mensagem de agradecimento por jogar ao final do jogo
"""
from random import randint


class GuessNumber:
    """Class GuessNumber."""

    def __init__(self):
        """-> Constructor.

        Initialize the game.
        """
        self.range = (1, 100)
        self.secret_number = randint(self.range[0], self.range[1])
        self.attempts = 0

    def __str__(self) -> str:
        """-> String representation of the object.

        :return: String representation of the object
        :rtype: str
        """
        return f'O número secreto é {self.secret_number}'

    def __repr__(self) -> str:
        """-> String representation of the object.

        :return: String representation of the object
        :rtype: str
        """
        return f'O número secreto é {self.secret_number}'

    def start(self) -> None:
        """-> Start the game.

        :return: None
        """
        print(
            '\n',
            ' Bem-vindo ao jogo de adivinhação! '.center(50, '='),
            end='\n\n',
        )
        print(
            f'Pensei em um número inteiro entre '
            f'{self.range[0]} e {self.range[1]}. Tente adivinhar...'
        )
        self.play()

    def play(self) -> None:
        """-> Play the game.

        :return: None
        """
        while True:
            try:
                self.attempts += 1
                guess = int(input('Tente adivinhar o número: '))
                if guess == self.secret_number:
                    print(
                        '\n',
                        f'Parabéns! Você acertou em '
                        f'{self.attempts} tentativas!',
                    )
                    if self.play_again():
                        self.__init__()
                        print('\n', 'Novo jogo iniciado! '.center(50, '-'))
                    else:
                        print(' Obrigado por jogar! '.center(50, '='))
                        break
                elif self.secret_number > guess > self.range[0]:
                    print(
                        f'O número secreto é maior '
                        f'que {guess}. Tente novamente!'
                    )
                elif self.secret_number < guess < self.range[1]:
                    print(
                        f'O número secreto é menor '
                        f'que {guess}. Tente novamente!'
                    )
                else:
                    print(
                        f'Você deve digitar um número '
                        f'entre {self.range[0]} e '
                        f'{self.range[1]}! '.center(50, '_')
                    )
            except ValueError:
                print(' Você deve digitar um número inteiro! '.center(50, '_'))

    @staticmethod
    def play_again() -> bool:
        """-> Ask if the user wants to play again.

        :return: True if the user wants to play again, False otherwise
        """
        while True:
            try:
                answer = input('Deseja jogar novamente? [s/numero] ')
                if answer.strip().lower()[0] == 's':
                    return True
                if answer.strip().lower()[0] == 'numero':
                    return False
                print(
                    'Resposta inválida! Digite "s" para sim ou '
                    '"numero" para não.'
                )
            except ValueError:
                print(
                    'Resposta inválida! Digite "s" para sim ou "numero" '
                    'para não.'
                )


def main():
    """-> Main function.

    :return: None
    """
    game = GuessNumber()
    game.start()


if __name__ == '__main__':
    main()
