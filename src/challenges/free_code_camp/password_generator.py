# -*- coding: utf-8 -*-
r"""password_generator.py in: 2022-05-05.

Python version: 3.10.0
"""
from random import choice
from string import ascii_letters, digits, punctuation

from tests.loguru_conf import logger


class GeradorDeSenhas:
    """Gerador de senhas.

    Essa classe gera senhas aleatórias.

    O usuário pode definir o tamanho da senha e o número de senhas a serem
    geradas.

    O módulo ‘string’ do Python é utilizado para obter as constantes de
    caracteres que contém números, letras e caracteres especiais.

    O módulo random do Python é utilizado para buscar caracteres aleatórios das
    constantes do módulo ‘string’.

    """

    def __init__(self, tamanho: int = 8, numero_de_senhas: int = 1) -> None:
        """Inicializa o gerador de senhas.

        :param tamanho: quantidade de caracteres da senha.
        :type tamanho: int
        :param numero_de_senhas: quantidade de senhas a serem geradas.
        :type numero_de_senhas: int

        """
        self.tamanho = tamanho
        self.numero_de_senhas = numero_de_senhas
        self.caracteres = ascii_letters + digits + punctuation
        self.mensagens = {
            'bem_vindo': ' Bem-vindo ao gerador de senhas! ',
            'tamanho': 'A senha deve ter entre 8 e 128 caracteres.',
            'numero_de_senhas': 'A quantidade de senhas deve ser entre '
                                '1 e 100.',
            'dicas': {
                1: '\t- sua senha deve ter entre 8 e 128 caracteres;',
                2: '\t- a quantidade de senhas a serem geradas deve ser entre '
                   '1 e 100;',
                3: '\t- digite somente números inteiros e positivos.',
            },
            'saida': 'Abaixo estão as senhas geradas:',
            'fim': ' Fim do programa. ',
        }

    def interface_usuario(self):
        """Obtém as entradas do usuário.

        O tamanho da senha é definido pelo usuário, porém não pode ser
        menor que 8 ou maior que 128.

        O número de senhas a serem geradas é definido pelo usuário, porém
        não pode ser menor que 1 ou maior que 100.

        Este método verifica se o tamanho da senha e o número de senhas
        são inteiros e positivos.

        """
        print(self.mensagens['bem_vindo'].center(60, '='), end='\n\n')
        while True:
            print(
                'Dicas:',
                self.mensagens['dicas'][1],
                self.mensagens['dicas'][2],
                self.mensagens['dicas'][3],
                sep='\n',
                end='\n\n',
            )
            try:
                self.tamanho = int(input('Tamanho da senha: '))
                if self.tamanho < 8 or self.tamanho > 128:
                    raise ValueError(self.mensagens['tamanho'])
                self.numero_de_senhas = int(input('Quantidade de senhas: '))
                if self.numero_de_senhas < 1 or self.numero_de_senhas > 100:
                    raise ValueError(self.mensagens['numero_de_senhas'])
                break
            except ValueError as erro:
                logger.error(erro)
                print(erro, end='\n\n')
                # print('Digite um número inteiro.')
                continue

    def gerar_senha(self) -> list:
        """Gera senhas aleatórias.

        :return: lista de senhas.
        :rtype: list

        """
        senhas = []
        for _ in range(self.numero_de_senhas):
            senha = ''
            for _ in range(self.tamanho):
                senha += choice(self.caracteres)
            senhas.append(senha)
        return senhas

    def gerar(self) -> object:
        """Chama a ‘interface’ com o usuário.

        :return: chamada ao método gerar_senha().
        :rtype: object
        """
        self.interface_usuario()
        return self.__str__()

    def __str__(self) -> object:
        """Retorna as senhas geradas.

        :return: corpo da mensagem de saída.
        :rtype: object
        """
        return print(
            self.mensagens['saida'],
            '\n'.join(self.gerar_senha()),
            self.mensagens['fim'].center(60, '='),
            sep='\n\n',
        )

    def __repr__(self) -> str:
        """Representação do objeto.

        :return: representação do objeto.
        :rtype: str
        """
        return (
            f'<{self.__class__.__name__}> {self.__class__.__doc__}\n'
            f'{self.__class__.__module__} {self.__dict__}'
        )


def main():
    """Função principal."""
    gerador = GeradorDeSenhas()
    gerador.gerar()
    # print(repr(gerador))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
