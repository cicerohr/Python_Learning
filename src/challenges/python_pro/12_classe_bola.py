# -*- coding: utf-8 -*-
r"""12_classe_bola.py in: 2022-04-27.

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


def main():
    """Função principal."""
    bola1 = Bola('Vermelha', 10, 'Plástico')
    print(bola1)
    bola1.trocar_cor('Amarela')
    bola1.mostrar_cor()
    print(bola1)
    print(repr(bola1))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
