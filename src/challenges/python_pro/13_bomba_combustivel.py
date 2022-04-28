# -*- coding: utf-8 -*-
r"""13_bomba_combustivel.py in: 2022-04-27.

Python version: 3.10.0

Classe Bomba de Combustível: Faça um programa completo utilizando classes e
métodos que:

Possua uma classe chamada BombaCombustivel, com no mínimo esses atributos:
    * tipo_combustivel;
    * valor_litro;
    * quantidade_combustivel_bomba.
Possua no mínimo esses métodos:
    * abastecer_por_valor() — método onde é informado o valor a ser abastecido
        e mostra a quantidade de litros colocada no veículo;

    * abastecer_por_litro() — método onde é informado a quantidade em litros de
        combustível e mostra o valor a ser pago pelo cliente;

    * alterar_valor() — altera o valor do litro do combustível;

    * alterar_combustivel() — altera o tipo do combustível;

    * abastecer_bomba() — acrescentar combustível na bomba.

Obs.: sempre que acontecer um abastecimento é necessário atualizar a quantidade
de combustível total na bomba.

Não permitir abastecer o tanque com litros negativos na bomba.
"""
from tests.loguru_conf import logger


class BombaCombustivel:
    """Classe Bomba de Combustível.

    Atributos:
        * tipo_combustivel;
        * valor_litro;
        * quantidade_combustivel_bomba.

    Testes:
        >>> bomba = BombaCombustivel('Gasolina', 4.59, 100)
        >>> bomba.abastecer_por_valor(100)
        Abastecido com R$ 100.
        Litros: 21.79.
        >>> bomba.abastecer_por_litro(50)
        Abastecido com 50.00 litros.
        Valor a pagar: R$ 229.50.
        >>> bomba.alterar_valor(5.59)
        Valor do litro alterado para R$ 5.59
        >>> bomba.abastecer_por_litro(50)
        Não há combustível suficiente na bomba!
        Combustível restante: 28.21 litros.
        >>> bomba.abastecer_bomba(100)
        >>> bomba.abastecer_por_litro(-50)
        Não é possível abastecer com valor negativo!
        >>> bomba.abastecer_por_valor(-100)
        Não é possível abastecer com valor negativo!
    """

    def __init__(
        self,
        tipo_combustivel: str,
        valor_litro: float,
        quantidade_combustivel_bomba: float,
    ) -> None:
        """Inicialização da classe.

        :param tipo_combustivel: qual combustível.
        :param valor_litro: preço do litro do combustível.
        :param quantidade_combustivel_bomba: combustível restante na bomba.
        """
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel_bomba = quantidade_combustivel_bomba

    def _verificar_bomba(self, litros_abastecer: float) -> bool:
        """Informar se há combustível suficiente na bomba.

        Verifica se a quantidade de combustível solicitada é maior que a
        quantidade de combustível restante na bomba.

        :param litros_abastecer: quantidade de litros a ser abastecida.
        :return: True se houver combustível suficiente na bomba. False se não.
        """
        if litros_abastecer > self.quantidade_combustivel_bomba:
            print(
                f'Não há combustível suficiente na bomba!\n'
                f'Combustível restante: '
                f'{self.quantidade_combustivel_bomba:.2f} litros.'
            )
            logger.error(
                f'Não há combustível suficiente na bomba!\n'
                f'Combustível restante: {self.quantidade_combustivel_bomba}'
            )
            return False
        if litros_abastecer < 0:
            print('Não é possível abastecer com valor negativo!')
            logger.error('Não é possível abastecer com valor negativo!')
            return False
        return True

    def abastecer_por_valor(self, valor_abastecer: float) -> None:
        """Abastecer por valor.

        :param valor_abastecer: valor a ser abastecido.
        """
        if self._verificar_bomba(valor_abastecer / self.valor_litro):
            self.quantidade_combustivel_bomba -= (
                valor_abastecer / self.valor_litro
            )
            print(
                f'Abastecido com R$ {valor_abastecer}.\n'
                f'Litros: {valor_abastecer / self.valor_litro:.2f}.'
            )
            logger.info(
                f'Abastecimento realizado com sucesso!\n'
                f'Combustível restante: '
                f'{self.quantidade_combustivel_bomba:.2f} litros'
            )

    def abastecer_por_litro(self, litros_abastecer: float) -> None:
        """Abastecer por litro.

        :param litros_abastecer: quantidade de litros a ser abastecida.
        """
        if self._verificar_bomba(litros_abastecer):
            self.quantidade_combustivel_bomba -= litros_abastecer
            print(
                f'Abastecido com {litros_abastecer:.2f} litros.\n'
                f'Valor a pagar: R$ {litros_abastecer * self.valor_litro:.2f}.'
            )
            logger.info(
                f'Abastecimento realizado com sucesso!\n'
                f'Combustível restante: {self.quantidade_combustivel_bomba}'
            )

    def abastecer_bomba(self, litros_abastecer: float) -> None:
        """Acrescenta combustível na bomba.

        :param litros_abastecer: quantidade de litros a ser abastecida.
        """
        if litros_abastecer > 0:
            self.quantidade_combustivel_bomba += litros_abastecer
            logger.info(
                f'Abastecimento realizado com sucesso!\n'
                f'Combustível restante: {self.quantidade_combustivel_bomba}'
            )
        else:
            print('Valor inválido.')

    def alterar_valor(self, novo_valor: float) -> None:
        """Altera o valor do litro.

        :param novo_valor: novo valor do litro.
        """
        self.valor_litro = novo_valor
        print(f'Valor do litro alterado para R$ {novo_valor}')
        logger.info(f'Valor do litro alterado para R$ {novo_valor}')

    def __str__(self):
        """String do objeto."""
        return (
            f'Bomba de {self.tipo_combustivel}.\n'
            f'Valor do litro: R$ {self.valor_litro:.2f}.\n'
            f'Combustível restante: '
            f'{self.quantidade_combustivel_bomba:.2f} litros.'
        )

    def __repr__(self):
        """Representação da classe."""
        return (
            f'<{self.__class__.__name__}> {self.__class__.__doc__}\n'
            f'{self.__class__.__module__} {self.__dict__}'
        )


def main():
    """Função principal."""
    bomba = BombaCombustivel('Gasolina', 4.59, 100)
    print(bomba, '-' * 60, sep='\n')
    bomba.abastecer_por_valor(100)
    print(bomba, '-' * 60, sep='\n')
    bomba.abastecer_por_litro(100)
    print(bomba, '-' * 60, sep='\n')
    bomba.abastecer_bomba(100)
    print(bomba, '-' * 60, sep='\n')
    bomba.alterar_valor(5.59)
    print(bomba, '-' * 60, sep='\n')
    bomba.abastecer_por_litro(50)
    print(bomba, '-' * 60, sep='\n')
    print(repr(bomba))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
