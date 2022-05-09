# -*- coding: utf-8 -*-
r"""guess_number_computer.py in: 2022-05-02.

Python version: 3.10.0

Testes:
    >>> computador = ComputadorAdivinhaNumero(1, 100)
    >>> computador.numero_secreto = 1
    >>> computador.adivinhar_numero()
    50
    >>> computador.adivinhar_numero_abaixo()
    25
    >>> computador.adivinhar_numero_abaixo()
    12
    >>> computador.adivinhar_numero_abaixo()
    6
    >>> computador.adivinhar_numero_abaixo()
    3
    >>> computador.adivinhar_numero_abaixo()
    1
    >>> computador.obter_lista_tentados()
    [50, 25, 12, 6, 3, 1]
"""
from tests.loguru_conf import logger


class ComputadorAdivinhaNumero:
    """Classe para o computador adivinhar o número."""

    def __init__(self, minimo: int, maximo: int) -> None:
        """Inicialização da classe.

        :param maximo: valor máximo do número.
        :type maximo: int
        :param minimo: valor mínimo do número.
        :type minimo: int
        """
        self.minimo = minimo
        self.maximo = maximo
        self.numero_tentado = None
        self.lista_numeros_tentados = []

    def adivinhar_numero(self) -> int:
        """Método para o computador adivinhar o número.

        :return: número adivinhado.
        :rtype: int
        """
        self.numero_tentado = (self.minimo + self.maximo) // 2
        self.lista_numeros_tentados.append(self.numero_tentado)
        return self.numero_tentado

    def adivinhar_numero_acima(self) -> int:
        """Método que aumenta o número adivinhado para cima.

        :return: número adivinhado acima.
        :rtype: int
        """
        self.minimo = self.numero_tentado + 1
        return self.adivinhar_numero()

    def adivinhar_numero_abaixo(self) -> int:
        """Método que diminui o número adivinhado para baixo.

        :return: número adivinhado abaixo.
        :rtype: int
        """
        self.maximo = self.numero_tentado - 1
        return self.adivinhar_numero()

    def obter_lista_tentados(self) -> list:
        """Retorna a lista de números adivinhados.

        :return: lista de números adivinhados.
        :rtype: list
        """
        return self.lista_numeros_tentados

    def obter_numero_tentativas(self) -> int:
        """Retorna o tamanho da lista de números adivinhados.

        :return: tamanho da lista de números adivinhados.
        :rtype: int
        """
        return len(self.lista_numeros_tentados)

    def __str__(self) -> str:
        """Retorna mensagem da classe."""
        return f"""O número é {self.numero_tentado}?
        Você adivinhou em {self.obter_numero_tentativas()} tentativas.
        {self.obter_lista_tentados()}
        """

    def __repr__(self) -> str:
        """Representação do objeto."""
        return (
            f'<{self.__class__.__name__}> {self.__class__.__doc__}\n'
            f'{self.__class__.__module__} {self.__dict__}'
        )


def tratar_entrada(entrada: str, minimo: int, maximo: int) -> int:
    """Trata a entrada do usuário.

    :param entrada: entrada do usuário.
    :type entrada: str
    :param minimo: valor mínimo do número.
    :type minimo: int
    :param maximo: valor máximo do número.
    :type maximo: int
    :return: número digitado pelo usuário.
    :rtype: int
    """
    while True:
        try:
            entrada = int(entrada)
            if minimo <= entrada <= maximo:
                return entrada
            raise ValueError
        except ValueError:
            print(
                f'Entrada inválida. Digite um número '
                f'entre {minimo} e {maximo}.'
            )
            entrada = input('Digite um número inteiro: ')
            continue


def main():
    """Função principal."""
    n_minimo = 1
    n_maximo = 100
    numero_secreto = tratar_entrada(
        input(f'Digite um número entre {n_minimo} e {n_maximo}: '),
        n_minimo,
        n_maximo
    )
    computador = ComputadorAdivinhaNumero(n_minimo, n_maximo)
    computador.adivinhar_numero()
    while True:
        if numero_secreto == computador.numero_tentado:
            print(computador)
            break
        if numero_secreto < computador.numero_tentado:
            computador.adivinhar_numero_abaixo()
        elif numero_secreto > computador.numero_tentado:
            computador.adivinhar_numero_acima()
        else:
            print('Você digitou um número inválido!')
            break
    print(repr(computador))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
