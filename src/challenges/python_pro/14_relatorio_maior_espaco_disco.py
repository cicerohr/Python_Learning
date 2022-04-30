# -*- coding: utf-8 -*-
r"""14_relatorio_maior_espaco_disco.py in: 2022-04-28.

Python version: 3.10.0

Controle de cotas de disco.

A empresa ACME Inc., uma organização com mais de 1 500 funcionários, está
tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar
resolver este problema, o Administrador de Rede precisa saber qual o espaço em
disco ocupado pelas contas dos usuários, e identificar os usuários com maior
espaço ocupado. Através de um aplicativo baixado da ‘internet’, ele conseguiu
gerar o arquivo, chamado "usuarios.txt".

Neste arquivo, o primeiro campo corresponde ao ‘login’ do usuário e o segundo
ao espaço em disco ocupado pelo seu diretório home. A partir deste arquivo,
você deve criar um programa que gere um relatório, chamado "relatório.txt",
no seguinte formato:

        ACME Inc.           Uso do espaço em disco pelos usuários
        ----------------------------------------------------------
        Nr.  Usuário        Espaço utilizado     % do uso

        1    alexandre       434,99 MB            16,85%
        2    anderson       1187,99 MB            46,02%
        3    antonio         117,73 MB             4,56%
        4    carlos           87,03 MB             3,37%
        5    cesar             0,94 MB             0,04%
        6    rosemary        752,88 MB            29,16%

        Espaço total ocupado: 2581,57 MB
        Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em
memória, caso sejam necessários, para agilizar a execução do programa.
A conversão do espaço ocupado em disco, de ‘bytes’ para ‘megabytes’ deverá ser
feita através de uma função separada, que será chamada pelo programa principal.
O cálculo do percentual de uso também deverá ser feito através de uma função,
que será chamada pelo programa principal.

Recursos adicionais: opcionalmente, desenvolva as seguintes funcionalidades:
    * Mostrar apenas os 'n' primeiros em uso, definido pelo usuário.

"""
from tests.loguru_conf import logger


class RelatorioControleCotasDisco:
    """Relatório de controle de cotas de disco."""

    def __init__(self, nome_arquivo, n_primeiros_usuarios):
        """Método construtor."""
        self.MEGABYTE = 1_048_576
        self.nome_arquivo = nome_arquivo
        self.n_primeiros_usuarios = n_primeiros_usuarios
        self.espaco_ocupado = 2581.57
        self.dados = []
        self.ler_arquivo()
        self.ordenar_dados()
        self.gerar_relatorio()

    def ler_arquivo(self):
        """Ler arquivo."""
        with open(self.nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip().split()
                bytes_convertido = self.converter_bytes_megabytes(
                    int(linha[1])
                )
                porcentagem_uso = self.calcular_porcentagem_uso(
                    self.espaco_ocupado, bytes_convertido
                )
                self.dados.append(
                    [linha[0], bytes_convertido, porcentagem_uso])
        logger.info(f'Lido arquivo {self.nome_arquivo}')
        logger.info(f'Dados lidos: {self.dados}')

    def ordenar_dados(self):
        """Ordenar dados."""
        self.dados.sort(key=lambda x: int(x[1]), reverse=True)
        logger.info(f'Dados ordenados: {self.dados}')

    @staticmethod
    def converter_bytes_megabytes(bytes_):
        """Converter bytes para megabytes."""
        MEGABYTE = 1_048_576
        return round(bytes_ / MEGABYTE, 2)

    @staticmethod
    def calcular_porcentagem_uso(bytes_, uso_):
        """Calcular percentual de uso."""
        return round(uso_ / bytes_ * 100, 2)

    def gerar_relatorio(self):
        """Gerar relatório."""
        with open('relatorio.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write(
                'ACME Inc.\t\tUso do espaço em disco pelos usuários\n'
                '--------------------------------------------------\n'
                'Nr.\tUsuário\t\tEspaço utilizado\t% do uso\n\n'
            )
            for i, linha in enumerate(self.dados):
                if i < self.n_primeiros_usuarios:
                    nome = linha[0].ljust(10)
                    espaco_utilizado = str(linha[1]).rjust(12)
                    percentual_uso = str(linha[2]).rjust(6)
                    arquivo.write(
                        f'{i + 1} - {nome}\t'
                        f'{espaco_utilizado} MB\t\t'
                        f'{percentual_uso} %\n'
                    )
            arquivo.write(
                f'\nEspaço total ocupado: {self.espaco_ocupado} MB\n'
                f'Espaço médio ocupado: {round(self.espaco_ocupado / len(self.dados), 2)} MB\n'
            )

    def mostrar_relatorio(self):
        """Mostrar relatório."""
        with open('relatorio.txt', 'r', encoding='utf-8') as arquivo:
            print(arquivo.read())

    def __str__(self):
        """String do objeto."""
        return f'Relatório de controle de cotas de disco.\n' \
               f'Nome do arquivo: {self.nome_arquivo}\n' \
               f'Número de usuários: {self.n_primeiros_usuarios}\n' \
               f'Espaço ocupado: {self.espaco_ocupado} MB\n' \
               f'Dados ordenados: {self.dados}\n' \
               f'Relatório gerado: relatorio.txt'

    def __repr__(self):
        """Representação da classe."""
        return (
            f'<{self.__class__.__name__}> {self.__class__.__doc__}\n'
            f'{self.__class__.__module__} {self.__dict__}'
        )


def main():
    """Função principal."""
    relatorio = RelatorioControleCotasDisco('usuarios.txt', 8)
    relatorio.mostrar_relatorio()
    print(relatorio, end='\n\n')
    print(repr(relatorio))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
