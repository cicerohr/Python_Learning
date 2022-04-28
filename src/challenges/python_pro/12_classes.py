# -*- coding: utf-8 -*-
r"""12_classes.py in: 2022-04-27.

Python version: 3.10.0

Classe Bola: Crie uma classe que modele uma bola:
    - A Atributos: Cor, circunferência, material
    - B Métodos: trocaCor e mostraCor
"""
from tests.loguru_conf import logger


class Bola:
    """Classe que modela uma bola."""

    def __init__(self, cor: str, circunferencia: float, material: str) -> None:
        """Inicialização da classe.

        :param cor: cor da bola.
        :param circunferencia: circunferência da bola.
        :param material: material da bola.
        :rtype: None
        """
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self, nova_cor: str) -> None:
        """Troca a cor da bola.

        :param nova_cor: nova cor da bola.
        :rtype: None
        """
        self.cor = nova_cor
        logger.info(f'Bola {self.cor}')

    def mostrar_cor(self):
        """Mostra a cor da bola."""
        logger.info(f'Bola {self.cor}')

    def __str__(self) -> str:
        """Retorna a cor da bola.

        :return: cor da bola.
        :rtype: str
        """
        return f'Bola {self.cor}.'

    def __repr__(self) -> str:
        """Representação da classe.

        :return: representação da classe.
        :rtype: str
        """
        return (
            f'<class {self.__class__.__name__}> {self.__class__.__doc__}'
            f'\n{self.__class__.__module__} {self.__dict__}'
        )


class Quadrado:
    """Classe que modela um quadrado."""

    def __init__(self, lado: float) -> None:
        """Inicialização da classe.

        :param lado: lado do quadrado.
        :rtype: None
        """
        self.lado = lado

    def mudar_lado(self, novo_lado: float) -> None:
        """Troca o valor do lado do quadrado.

        :param novo_lado: novo lado do quadrado.
        :rtype: None
        """
        self.lado = novo_lado
        logger.info(f'Quadrado {self.lado}')

    def calcular_area(self) -> float:
        """Calcula a área do quadrado.

        :return: área do quadrado.
        :rtype: float
        """
        return self.lado ** 2

    def __str__(self) -> str:
        """Retorna o valor do lado do quadrado.

        :return: valor do lado do quadrado.
        :rtype: str
        """
        return f'Quadrado de lado {self.lado}.'

    def __repr__(self) -> str:
        """Representação da classe.

        :return: representação da classe.
        :rtype: str
        """
        return (
            f'<class {self.__class__.__name__}> {self.__class__.__doc__}'
            f'\n{self.__class__.__module__} {self.__dict__}'
        )


class Pessoa:
    """Classe que modela uma pessoa.

    Atributos: nome, idade, peso e altura da pessoa.

    Métodos: envelhecer, engordar, emagrecer, crescer.

    Obs.: por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela
    menor que 21 anos, ela deve crescer 0,5 cm.

    Testes:
    >>> p = Pessoa('João', 19, 80, 1.75)
    >>> p.envelhecer()
    >>> p.idade
    20
    >>> p.altura
    175.5
    >>> p.engordar(10)
    >>> p.peso
    90
    >>> p.emagrecer(10)
    >>> p.peso
    80
    >>> p.envelhecer()
    >>> p.idade
    21
    >>> p.altura
    175.5
    """

    def __init__(
        self, nome: str, idade: int, peso: float, altura: float
    ) -> None:
        """Inicialização da classe.

        :param nome: nome da pessoa.
        :param idade: idade da pessoa.
        :param peso: peso da pessoa.
        :param altura: altura em metros da pessoa.
        :rtype: None
        """
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura * 100  # converte para cm

    def envelhecer(self) -> None:
        """Envelhece a pessoa.

        :rtype: None
        """
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)
        logger.info(f'{self.nome} envelheceu.')

    def engordar(self, kg: float) -> None:
        """Engorda a pessoa.

        :param kg: quantidade de kg a engordar.
        :rtype: None
        """
        self.peso += kg
        logger.info(f'{self.nome} engordou {kg} kg.')

    def emagrecer(self, kg: float) -> None:
        """Emagrece a pessoa.

        :param kg: quantidade de kg a emagrecer.
        :rtype: None
        """
        self.peso -= kg
        logger.info(f'{self.nome} emagreceu {kg} kg.')

    def crescer(self, cm: float) -> None:
        """Crescimento da pessoa.

        :param cm: quantidade de cm a crescer.
        :rtype: None
        """
        self.altura += cm
        logger.info(f'{self.nome} cresceu {cm} cm.')

    def __str__(self) -> str:
        """Retorna a representação da pessoa.

        :return: representação da pessoa.
        :rtype: str
        """
        return (
            f'{self.nome} tem {self.idade} anos, pesa {self.peso} kg e '
            f'{self.altura} cm de altura.'
        )

    def __repr__(self) -> str:
        """Representação da classe.

        :return: representação da classe.
        :rtype: str
        """
        return (
            f'<class {self.__class__.__name__}> {self.__class__.__doc__}'
            f'\n{self.__class__.__module__} {self.__dict__}'
        )


def main():
    """Função principal."""
    bola1 = Bola('Vermelha', 10, 'Plástico')
    print(bola1)
    bola1.trocar_cor('Amarela')
    bola1.mostrar_cor()
    print(bola1)
    print(repr(bola1))
    print('-' * 60)
    quadrado1 = Quadrado(10)
    print(quadrado1)
    quadrado1.mudar_lado(20)
    print(quadrado1.calcular_area())
    print(quadrado1)
    print(repr(quadrado1))
    print('-' * 60)
    pessoa1 = Pessoa('João', 16, 80.0, 1.80)
    print(pessoa1)
    pessoa1.envelhecer()
    print(pessoa1)
    pessoa1.envelhecer()
    print(pessoa1)
    pessoa1.envelhecer()
    print(pessoa1)
    print(repr(pessoa1))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
