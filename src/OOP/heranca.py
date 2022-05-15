# -*- coding: utf-8 -*-
r"""heranca.py in: 2022-05-11.

@author: Fabio Kon
@modified by: Cícero
@link: https://gitlab.com/ccsl-usp/LabPOO/-/blob/master/heranca/poligono.py
"""
from abc import ABC, abstractmethod

from tests.loguru_conf import logger


class Poligono(ABC):
    """Classe abstrata base para um polígono.

    Atributos:
        nome (str): nome do polígono.
        numero_de_lados (int): quantidade de lados do polígono.
        lados (list): lista dos lados do polígono.

    Métodos:
        __init__(self, nome, numero_de_lados): inicializa o objeto.
        eh_regular(): verifica se o polígono é regular.
        obter_lados(): obtém os valores dos lados (abstractmethod).
        calcular_area(): calcula a área do polígono.
        calcular_perimetro(): retorna o perímetro do polígono.
        numero_de_diagonais(): retorna o número de diagonais.
        __repr__(self): retorna uma representação do objeto.
    """

    def __init__(self, nome: str, numero_de_lados: int) -> None:
        """Construtor da classe Polígono.

        :param nome: nome do polígono.
        :type nome: str
        :param numero_de_lados: quantidade de lados do polígono.
        :type numero_de_lados: int.
        """
        self.nome = nome
        self.numero_de_lados = numero_de_lados
        self.lados = [0 for _ in range(numero_de_lados)]

    def eh_regular(self) -> bool:
        """Verifica se o polígono é regular.

        Um polígono é regular se todos os lados são iguais.

        :return: verdadeiro se o polígono é regular.
        :rtype: bool.
        """
        return len(set(self.lados)) == 1

    def obter_lados(self) -> None:
        """Obtém os valores dos lados do polígono."""
        self.lados = [
            float(input(f'{self.nome} - Lado {str(i + 1)}: '))
            for i in range(self.numero_de_lados)
        ]

    @abstractmethod
    def calcular_area(self) -> float:
        """Calcula a área do polígono.

        Método abstrato que gera essa exceção para exigir que classes
        derivadas substituam esse método.

        :return: área do polígono.
        :rtype: float.
        """
        raise NotImplementedError(
            'Subclasses precisam implementar o método calcular_area()'
        )

    def calcular_perimetro(self) -> float:
        """Calcula o perímetro de um polígono.

        :return: perímetro do polígono.
        :rtype: float.
        """
        return sum(self.lados)

    def numero_de_diagonais(self) -> int:
        """Calcula o número de diagonais do polígono.

        :return: número de diagonais do polígono.
        :rtype: int.
        """
        return (self.numero_de_lados * (self.numero_de_lados - 3)) // 2

    def __repr__(self) -> str:
        """Representação do objeto."""
        return (
            f'{self.__class__.__name__}()\n'
            f'{self.__class__.__doc__}\n'
            f'{self.__class__.__module__} {self.__dict__}\n'
        )


class Triangulo(Poligono):
    """Classe que representa um triângulo.

    Atributos:
        nome (str): nome do polígono.

    Métodos:
        __init__(): construtor da classe.
        eh_triangulo(): verifica se é um triângulo válido.
        determinar_tipo_triangulo_lados(): determina o tipo de triângulo.
        calcular_area(): calcula a área do triângulo.
        __str__(): retorna uma ‘string’ com os dados do triângulo.
    """

    def __init__(self) -> None:
        """Construtor da classe Triangulo."""
        self.nome = 'Triângulo'
        # chama o construtor da classe pai (Polígono)
        super().__init__(self.nome, 3)

    def eh_triangulo(self) -> bool:
        """Verifica se os lados formam um triângulo.

        :return: True se os lados formam um triângulo e False se não.
        :rtype: bool
        """
        a, b, c = self.lados
        if a + b > c and a + c > b and b + c > a:
            return True
        return False

    def determinar_tipo_triangulo_lados(self) -> str:
        """Determina o tipo de triângulo quanto aos lados.

        Retorna o tipo de triângulo.

        :return: tipo de triângulo.
        :rtype: str
        """
        a, b, c = self.lados
        if a == b and b == c and c == a:
            return 'equilátero'
        if a == b or b == c or c == a:
            return 'isósceles'
        return 'escaleno'

    def calcular_area(self) -> float:
        """Calcula a área do triângulo.

        Utiliza a fórmula de Heron.

        :return: área do triângulo.
        :rtype: float
        """
        a, b, c = self.lados
        # calcula o semiperímetro
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

    def __str__(self) -> str:
        """Retorna uma ‘string’ com os dados do triângulo."""
        a, b, c = self.lados
        if self.eh_triangulo():
            return (
                f'{self.nome} de lados {a}, {b} e {c} tem:\n'
                f'\tÁrea: {self.calcular_area():0.2f}\n'
                f'\tPerímetro: {self.calcular_perimetro():0.2f}\n'
                f'\tTipo: {self.determinar_tipo_triangulo_lados()}\n'
                f'\tÉ regular? {"sim" if self.eh_regular() else "não"}\n'
            )
        return f'Os lados {a}, {b} e {c} não formam um triângulo.'


class TrianguloRetangulo(Triangulo):
    """Classe que representa um triângulo retângulo.

    Atributos:
        nome (str): nome do triângulo.

    Métodos:
        __init__(): construtor da classe.
        eh_triangulo_retangulo(): verifica se é um triângulo retângulo é válido
        __str__(): retorna uma ‘string’ com os dados do triângulo retângulo.
    """

    def __init__(self) -> None:
        """Construtor da classe TrianguloRetangulo."""
        # chama o construtor da classe pai (Triangulo)
        super().__init__()
        self.nome = 'Triângulo Retângulo'

    def eh_triangulo_retangulo(self) -> bool:
        """Verifica se os lados formam um triângulo retângulo.

        Utiliza a fórmula de Pitágoras para verificar se os lados
        formam um triângulo retângulo.

        :return: True se os lados formam um triângulo retângulo e False se não.
        :rtype: bool
        """
        a, b, c = self.lados
        return (
                a ** 2 == b ** 2 + c ** 2
                or b ** 2 == a ** 2 + c ** 2
                or c ** 2 == a ** 2 + b ** 2
        )

    def __str__(self) -> str:
        """Retorna uma ‘string’ com os dados do triângulo retângulo."""
        a, b, c = self.lados
        if self.eh_triangulo() and self.eh_triangulo_retangulo():
            return (
                f'{self.nome} de lados {a}, {b} e {c} tem:\n'
                f'\tÁrea: {self.calcular_area():0.2f}\n'
                f'\tPerímetro: {self.calcular_perimetro():0.2f}\n'
                f'\tTipo: {self.determinar_tipo_triangulo_lados()}\n'
            )
        return f'Os lados {a}, {b} e {c} não formam um triângulo retângulo.'


class Retangulo(Poligono):
    """Classe que representa um retângulo.

    Atributos:
        nome (str): nome do polígono.

    Métodos:
        __init__(): construtor da classe.
        obter_lados(): obtém os valores dos lados do retângulo.
        calcular_area(): calcula a área do retângulo.
        calcular_diagonal(): calcula a diagonal do retângulo.
        __str__(): retorna uma ‘string’ com os dados do retângulo.
    """

    def __init__(self) -> None:
        """Construtor da classe Retangulo."""
        self.nome = 'Retângulo'
        # chama o construtor da classe pai (Polígono)
        super().__init__(self.nome, 4)

    def obter_lados(self):
        """Obtém os valores dos lados do retângulo."""
        lado1 = float(input(f'{self.nome} - Lado 1: '))
        lado2 = float(input(f'{self.nome} - Lado 2: '))
        self.lados = [lado1, lado2, lado1, lado2]

    def calcular_area(self) -> float:
        """Calcula a área do retângulo.

        :return: área do retângulo.
        :rtype: float
        """
        return self.lados[0] * self.lados[1]

    def calcular_diagonal(self) -> float:
        """Calcula a diagonal do retângulo.

        Utiliza a fórmula de Pitágoras para calcular a diagonal.

        :return: diagonal do retângulo.
        :rtype: float
        """
        return (self.lados[0] ** 2 + self.lados[1] ** 2) ** 0.5

    def __str__(self) -> str:
        """Retorna uma ‘string’ com os dados do retângulo."""
        return (
            f'{self.nome} de {self.lados[0]}x{self.lados[1]} tem:\n'
            f'\tÁrea: {self.calcular_area():0.2f}\n'
            f'\tPerímetro: {self.calcular_perimetro():0.2f}\n'
            f'\tDiagonal: {self.calcular_diagonal():0.2f}\n'
            f'\tNúmero de diagonais: {self.numero_de_diagonais()}\n'
            f'\tÉ regular? {"sim" if self.eh_regular() else "não"}\n'
        )


class Trapezio(Poligono):
    """Classe que representa um trapézio.

    Atributos:
        nome (str): nome do polígono.

    Métodos:
        __init__(): construtor da classe.
        obter_lados(): obtém os valores dos lados do trapézio.
        calcular_area(): calcula a área do trapézio.
        calcular_altura(): calcula a altura do trapézio.
        __str__(): retorna uma ‘string’ com os dados do trapézio.
    """

    def __init__(self) -> None:
        """Construtor da classe Trapezio."""
        self.nome = 'Trapézio'
        # chama o construtor da classe pai (Polígono)
        super().__init__(self.nome, 4)

    def obter_lados(self) -> None:
        """Obtém os valores dos lados do trapézio."""
        base_maior = float(input(f'{self.nome} - Base maior: '))
        base_menor = float(input(f'{self.nome} - Base menor: '))
        lado1 = float(input(f'{self.nome} - Lado 1: '))
        lado2 = float(input(f'{self.nome} - Lado 2: '))
        self.lados = [base_maior, base_menor, lado1, lado2]

    def calcular_area(self) -> float:
        """Calcula a área do trapézio.

        Utiliza a fórmula de Heron para calcular a área.

        :return: área do trapézio.
        :rtype: float
        """
        base_maior = self.lados[0]
        base_menor = self.lados[1]
        lado1 = self.lados[2]
        lado2 = self.lados[3]
        semiperimetro = (base_maior + base_menor + lado1 + lado2) / 2
        return (
                       semiperimetro
                       * (semiperimetro - base_maior)
                       * (semiperimetro - base_menor)
                       * (semiperimetro - lado1)
                       * (semiperimetro - lado2)
               ) ** 0.5

    def altura(self) -> float:
        """Calcula a altura do trapézio.

        A partir da área do trapézio e das bases, calcula a altura.

        A = h * (B + b) / 2 ∴ h = 2 * A / (B + b)

        :return: altura do trapézio.
        :rtype: float
        """
        return (self.calcular_area() * 2) / (self.lados[0] + self.lados[1])

    def __str__(self) -> str:
        """Retorna uma ‘string’ com os dados do trapézio.

        :return: dados do trapézio.
        :rtype: str
        """
        return (
            f'{self.nome} - base maior: {self.lados[0]}; '
            f'base menor: {self.lados[1]}; '
            f'lado 1: {self.lados[2]}; '
            f'lado 2: {self.lados[3]}\n'
            f'\tÁrea: {self.calcular_area():.2f}\n'
            f'\tPerímetro: {self.calcular_perimetro():.2f}\n'
            f'\tNúmero de diagonais: {self.numero_de_diagonais()}\n'
            f'\tAltura: {self.altura():.2f}\n'
            f'\tÉ regular? {"sim" if self.eh_regular() else "não"}\n'
        )


def main():
    """Função principal."""
    # retangulo = Retangulo()
    # retangulo.obter_lados()
    # print(retangulo)
    # print(repr(retangulo))
    # triangulo = Triangulo()
    # triangulo.obter_lados()
    # print(triangulo)
    # print(repr(triangulo))
    # triangulo_retangulo = TrianguloRetangulo()
    # triangulo_retangulo.obter_lados()
    # print(triangulo_retangulo)
    # print(repr(triangulo_retangulo))
    # trapezio = Trapezio()
    # trapezio.obter_lados()
    # print(trapezio)
    # print(repr(trapezio))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
