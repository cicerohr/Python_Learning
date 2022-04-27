# -*- coding: utf-8 -*-
r"""11_busca_maior_espaco_disco.py in: 2022-04-26.

Python version: 3.10.0

A empresa ACME Inc., uma empresa de 500 funcionários, está tendo problemas de
espaço em disco no seu servidor de arquivos. Para tentar resolver este
problema, o administrador de Rede precisa saber qual o espaço ocupado pelos
usuários, e identificar os usuários com maior espaço ocupado. Através de um
programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado
"usuarios.txt".

https://pythonpro.com.br/desafio-python-em-14-dias-aula-11/
"""
from tests.loguru_conf import logger


class BuscaMaiorEspacoDisco:
    """Classe BuscaMaiorEspacoDisco.

    Busca no arquivo usuarios.txt o usuário com maior espaço ocupado de disco.

    Formato do arquivo: 'usuario'        'espaco_ocupado'
    """

    def __init__(self) -> None:
        """Inicialização da classe.

        :rtype: None
        """
        self.usuarios = {}
        self.maior_espaco_ocupado = 0
        self.usuario = None
        self.arquivo = 'usuarios.txt'

    def __str__(self) -> str:
        """‘String’ do objeto.

        Retorna uma ‘string’ com o usuário e valor do maior espaço
        ocupado de disco.

        :return: ‘string’ com usuário e valor do maior espaço ocupado de disco.
        :rtype: str
        """
        return (
            f'O usuário {self.usuario} '
            f'ocupou o maior espaço de disco: {self.maior_espaco_ocupado}'
        )

    def __repr__(self) -> str:
        """Representação da classe.

        :return: Representação da classe.
        :rtype: str

        """
        return (
            f'<class {self.__class__.__name__}> {self.__class__.__doc__}'
            f'\n{self.__class__.__module__} {self.__dict__}'
        )

    def ler_arquivo(self, nome_arquivo) -> None:
        """Lê o arquivo e armazena os dados em um dicionário.

        :param nome_arquivo: nome do arquivo.
        """
        with open(nome_arquivo, 'r', encoding='UTF-8') as arquivo:
            for linha in arquivo:
                usuario, espaco_ocupado = linha.split()
                self.usuarios[usuario] = int(espaco_ocupado)
                if int(espaco_ocupado) > self.maior_espaco_ocupado:
                    self.maior_espaco_ocupado = int(espaco_ocupado)

    def buscar_usuario(self) -> str | None:
        """Busca o usuário com maior espaço ocupado de disco.

        :return: usuário com maior espaço ocupado de disco.
        :rtype: str
        """
        for usuario, _ in self.usuarios.items():
            if self.usuarios[usuario] == self.maior_espaco_ocupado:
                self.usuario = usuario
                return self.usuario
        return None


def main():
    """Main function."""
    logger.info('Início do programa.')
    busca = BuscaMaiorEspacoDisco()
    busca.ler_arquivo(busca.arquivo)
    print(
        f'\nUsuário com maior espaço ocupado de disco: '
        f'{busca.buscar_usuario()} ({busca.maior_espaco_ocupado}).\n'
    )
    print(busca)
    print(repr(busca))
    logger.info('Fim do programa.')


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
