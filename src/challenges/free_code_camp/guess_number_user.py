# -*- coding: utf-8 -*-
r"""guess_number_user.py in: 2022-05-02.

Python version: 3.10.0

Testes:
        >>> computador = UsuarioAdivinhaNumero()
        >>> numero_secreto = computador._numero_aleatorio = 50
        >>> computador.jogar(numero_secreto + 1)
        False
        >>> computador.obter_mensagem()
        'Errou! O número gerado é menor que 51.'
        >>> computador.jogar(numero_secreto - 1)
        False
        >>> computador.obter_mensagem()
        'Errou! O número gerado é maior que 49.'
        >>> computador.jogar(numero_secreto)
        True
        >>> computador.obter_mensagem()
        'Parabéns, você acertou em 3 tentativas!'
        >>> computador.obter_acertos()
        1
        >>> computador.obter_tentativas()
        3
        >>> computador.obter_erros()
        2
        >>> computador.obter_numeros_tentativas()
        [51, 49, 50]
"""
from random import randint
from typing import Any

from tests.loguru_conf import logger


class UsuarioAdivinhaNumero:
    """Classe UsuarioAdivinhaNumero.

    Classe que gera um número aleatório entre 1 e 100 e permite que o usuário
    tente adivinhar o número gerado.
    """

    def __init__(self):
        """Construtor da classe UsuarioAdivinhaNumero."""
        self._numero_aleatorio = self._gerar_numero()
        self.mensagem = ''
        self.tentativas = 0
        self.acerto = 0
        self.erros = 0
        self.erros_acerto = []

    @staticmethod
    def _gerar_numero() -> int:
        """Gera um número aleatório entre 1 e 100.

        :return: número aleatório entre 1 e 100.
        :rtype: int
        """
        return randint(1, 100)

    def jogar(self, numero: int) -> bool:
        """Usurário tenta adivinhar o número gerado.

        :param numero: número que o usuário tenta adivinhar.
        :type numero: int
        :return: True se o usuário acertou. False se o usuário errou.
        :rtype: bool
        """
        self.tentativas += 1
        self.erros_acerto.append(numero)
        if numero == self._numero_aleatorio:
            self.acerto += 1
            self.mensagem = (
                f'Parabéns, você acertou em {self.tentativas} '
                f'tentativa{"s" if self.tentativas > 1 else ""}!'
            )
            return True
        self.erros += 1
        if numero > self._numero_aleatorio:
            self.mensagem = f'Errou! O número gerado é menor que {numero}.'
        if numero < self._numero_aleatorio:
            self.mensagem = f'Errou! O número gerado é maior que {numero}.'
        return False

    def jogar_novamente(self):
        """Método que inicializa os atributos."""
        print(self.__str__())
        self.__init__()
        print('-' * 40, '\n')
        print('Novo número aleatório gerado...', '\n')
        print('Vamos jogar novamente!', '\n')

    def obter_acertos(self) -> int:
        """Retorna o número de acertos.

        :return: número de acertos.
        :rtype: int
        """
        return self.acerto

    def obter_erros(self) -> int:
        """Retorna o número de erros.

        :return: número de erros.
        :rtype: int
        """
        return self.erros

    def obter_tentativas(self) -> int:
        """Retorna o número de tentativas.

        :return: número de tentativas.
        :rtype: int
        """
        return self.tentativas

    def obter_numeros_tentativas(self) -> list:
        """Retorna uma lista com os números das tentativas.

        :return: números das tentativas.
        :rtype: list
        """
        return self.erros_acerto

    def obter_numero_aleatorio(self) -> int:
        """Retorna o número aleatório gerado.

        :return: número aleatório gerado.
        :rtype: int
        """
        return self._numero_aleatorio

    def obter_mensagem(self) -> str:
        """Retorna a mensagem para o usuário.

        :return: mensagem para o usuário.
        :rtype: str
        """
        return self.mensagem

    def __str__(self) -> str:
        """Retorna mensagem para o usuário."""
        return f"""{self.mensagem}
        Número aleatório: {self._numero_aleatorio}
        Tentativas: {self.tentativas}
        Erros: {self.erros}
        Tentativas: {self.erros_acerto}"""

    def __repr__(self) -> str:
        """Representação do objeto."""
        return (
            f'<{self.__class__.__name__}> {self.__class__.__doc__}\n'
            f'{self.__class__.__module__} {self.__dict__}'
        )


def verificar_numero(numero: Any) -> int:
    """Verifica se o número é um número inteiro.

    :param numero: número que o usuário tenta adivinhar.
    :type numero: Any
    :return: inteiro se o número for um número inteiro.
    :rtype: int
    """
    while True:
        try:
            numero = int(numero)
            if 1 <= numero <= 100:
                return numero
            raise ValueError
        except ValueError:
            print('Número inválido!')
            numero = input('Digite um número inteiro: ')
            continue


def main():
    """Função principal."""
    computador = UsuarioAdivinhaNumero()
    numero_usuario = verificar_numero(
        input('Digite um número entre 1 e 100: ')
    )
    while True:
        if computador.jogar(numero_usuario):
            jogar_novamente = input('Jogar novamente? (S/N): ')
            if jogar_novamente.strip().upper() == 'S':
                computador.jogar_novamente()
                numero_usuario = verificar_numero(
                    input('Digite um número entre 1 e 100: ')
                )
                continue
            print('Fim de jogo!')
            break
        print(computador.obter_mensagem())
        numero_usuario = verificar_numero(input('Faça outra tentativa: '))
    print(computador)
    print(repr(computador))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
