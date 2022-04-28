# -*- coding: utf-8 -*-
r"""13_bomba_combustivel.py in: 2022-04-27.

Python version: 3.10.0

Classe Bomba de Combustível: Faça um programa completo utilizando classes e
métodos que:

Possua uma classe chamada BombaCombustivel, com no mínimo esses atributos:
    * tipo_combustivel;
    * valor_litro;
    * quantidade_combustivel.
Possua no mínimo esses métodos:
    * abastecer_por_valor() — método onde é informado o valor a ser abastecido
        e mostra a quantidade de litros colocada no veículo;

    * abastecer_por_litro() — método onde é informado a quantidade em litros de
        combustível e mostra o valor a ser pago pelo cliente;

    * alterar_valor() — altera o valor do litro do combustível;

    * alterar_combustivel() — altera o tipo do combustível;

    * alterar_quantidade_combustivel() — altera a quantidade de combustível
        restante na bomba.

Obs.: sempre que acontecer um abastecimento é necessário atualizar a quantidade
de combustível total na bomba.
"""
from tests.loguru_conf import logger


class BombaCombustivel:
    """Classe Bomba de Combustível."""

    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        """Inicialização da classe."""
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        """Abastece por valor.

        Método onde é informado o valor a ser abastecido e mostra a quantidade
        de litros colocada no veículo.

        """
        logger.info(f'Abastecendo por valor...')
        self.quantidade_combustivel += valor / self.valor_litro
        logger.info(f'Quant. de combustível: {self.quantidade_combustivel}')
        logger.info(f'Valor total: {valor}')
        logger.info(f'Valor por litro: {self.valor_litro}')
        logger.info(f'Tipo de combustível: {self.tipo_combustivel}')
        logger.info(f'Abastecimento realizado com sucesso!')

    def abastecer_por_litro(self, litros):
        """Abastece por litro.

        Método onde é informado a quantidade em litros de combustível e mostra
        o valor a ser pago pelo cliente.

        """
        logger.info(f'Abastecendo por litro...')
        self.quantidade_combustivel -= litros
        logger.info(f'Quant. de combustível: {self.quantidade_combustivel}')
        logger.info(f'Valor total: {litros * self.valor_litro}')
        logger.info(f'Valor por litro: {self.valor_litro}')
        logger.info(f'Tipo de combustível: {self.tipo_combustivel}')
        logger.info(f'Abastecimento realizado com sucesso!')

    def alterar_valor(self, valor):
        """Altera o valor do litro do combustível."""
        logger.info(f'Alterando o valor do litro do combustível...')
        self.valor_litro = valor
        logger.info(f'Valor por litro: {self.valor_litro}')
        logger.info(f'Abastecimento realizado com sucesso!')

    def alterar_combustivel(self, tipo_combustivel):
        """Altera o tipo do combustível."""
        logger.info(f'Alterando o tipo do combustível...')
        self.tipo_combustivel = tipo_combustivel
        logger.info(f'Tipo de combustível: {self.tipo_combustivel}')
        logger.info(f'Abastecimento realizado com sucesso!')

    def alterar_quantidade_combustivel(self, quantidade_combustivel):
        """Altera a quantidade de combustível restante na bomba."""
        logger.info(f'Alterando a quan. de combustível restante na bomba...')
        self.quantidade_combustivel = quantidade_combustivel
        logger.info(f'Quant. de combustível: {self.quantidade_combustivel}')
        logger.info(f'Abastecimento realizado com sucesso!')

    def __str__(self):
        """Retorna uma ‘string’ com os dados da bomba."""
        return (
            f'Tipo de combustível: {self.tipo_combustivel}\n'
            f'Valor por litro: {self.valor_litro}\n'
            f'Quant. de combustível: {self.quantidade_combustivel}'
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
    bomba = BombaCombustivel('Gasolina', 4.50, 10)
    print(bomba, '-' * 60, sep='\n')
    bomba.abastecer_por_valor(100)
    print(bomba, '-' * 60, sep='\n')
    bomba.abastecer_por_litro(2)
    print(bomba, '-' * 60, sep='\n')
    bomba.alterar_valor(3.50)
    print(bomba, '-' * 60, sep='\n')
    bomba.alterar_combustivel('Álcool')
    print(bomba, '-' * 60, sep='\n')
    bomba.alterar_quantidade_combustivel(20)
    print(bomba, '-' * 60, sep='\n')
    print(bomba.__repr__())


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
