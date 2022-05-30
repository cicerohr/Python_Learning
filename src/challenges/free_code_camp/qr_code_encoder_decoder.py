# -*- coding: utf-8 -*-
r"""qr_code_encoder_decoder.py in: 2022-05-05.

Python version: 3.10.0
"""
import sys
from pathlib import Path

import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

from tests.loguru_conf import logger


class QRCodeEncoderDecoder:
    r"""Classe QRCodeEncoderDecoder.

    Essa classe codifica e descodifica um texto em um código QR.

    O pacote qrcode é utilizada para criar o código QR.
    Para mais informações sobre a biblioteca, consulte:
    https://pypi.org/project/qrcode/

    O usuário escolhe entres as opções:

    * Gerar um código QR com o texto digitado pelo usuário.
    * Descodificar um código QR e exibir o texto.
    * Sair do programa.

    A imagem é salva no diretório src/challenges/assets/qrcode/ do projeto.

    """

    def __init__(self):
        r"""Construtor da classe QRCodeEncoderDecoder."""
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        self.imagem = None
        self.texto = None
        self.imagem_caminho = (
            f'{Path(__file__).parent.parent}\\assets\\qrcode\\'
        )
        self.imagem_nome = ''
        self.imagem_extensao = '.png'
        self.menu = {
            1: 'Gerar QR',
            2: 'Decodificar QR',
            3: 'Sair',
        }

    def gerar_qr(self):
        r"""Método gerar_qr.

        Método para gerar um código QR com o texto digitado pelo usuário.

        """
        self.qr.add_data(self.texto)
        self.qr.make(fit=True)
        self.imagem = self.qr.make_image(fill_color='blue', back_color='white')
        self.imagem.save(
            f'{self.imagem_caminho}{self.imagem_nome}{self.imagem_extensao}'
        )

    def decodificar_qr(self):
        r"""Método descodificar_qr.

        Método para decodificar um código QR e exibir o texto.

        O método é chamado quando o usuário escolhe a opção 2 e pergunta
        o nome do arquivo.

        Há uma verificacao se o arquivo existe, se não existe,
        é exibido uma mensagem de erro.

        A imagem é recuperada do diretório src/challenges/assets/qrcode/ do
        projeto.

        Ao final, o método mostra o texto decodificado e o menu novamente.

        """
        self.imagem_caminho = (
            self.imagem_caminho + self.imagem_nome + self.imagem_extensao
        )
        logger.info(f'\n{self.imagem_caminho}')
        if Path(self.imagem_caminho).exists():
            try:
                self.imagem = Image.open(self.imagem_caminho)
                self.texto = decode(self.imagem)[0].data.decode('utf-8')
                logger.info(f'Texto decodificado: {self.texto}')
                print(f'Texto decodificado: {self.texto}')
            except IndexError:
                logger.error(
                    'Não foi possível decodificar o arquivo.',
                    f'Arquivo: {self.imagem_caminho}',
                )
                print('Não foi possível decodificar o arquivo.')
        else:
            logger.error(
                'Arquivo não encontrado.', f'Arquivo: {self.imagem_caminho}'
            )
            print('Arquivo não encontrado.')

        # self.mostrar_menu_novamente()

    def interface(self):
        r"""Método ‘interface’.

        Método para exibir a ‘interface’ de escolha do usuário.

        Um 'menu' é exibido para o usuário escolher entre as opções:

        * Gerar um código QR com o texto digitado pelo usuário.
        * Decodificar um código QR e exibir o texto.
        * Sair do programa.

        """
        print('\n', '=' * 80, end='\n\n')

        for key, value in self.menu.items():
            print(f'\t\t{key} - {value}')

        print('\n', '=' * 80, end='\n\n')

        while True:
            try:
                opcao = int(input('Digite a opção desejada: '))
                match opcao:
                    case 1:
                        self.texto = input('Digite o texto para gerar o QR: ')
                        self.imagem_nome = input('Digite o nome da imagem: ')
                        self.gerar_qr()
                        break
                    case 2:
                        self.imagem_nome = input(
                            'Digite o nome do arquivo QR para decodificar: '
                        )
                        self.decodificar_qr()
                        break
                    case 3:
                        print('Saindo...')
                        sys.exit()
                    case _:  # default
                        print('Opção inválida!')
                        continue
            except ValueError as error:
                logger.error(error)
                print('Opção inválida!')
                continue

        self.mostrar_info()
        self.mostrar_menu_novamente()

    def mostrar_menu_novamente(self):
        r"""Método mostrar_menu_novamente.

        Método para mostrar o menu novamente.

        """
        self.__init__()
        input('\nPressione <ENTER> para voltar ao menu...')
        self.interface()

    def mostrar_info(self):
        r"""Método mostrar_info.

        Método para mostrar as informações do código QR.

        """
        print('\n', self.__str__())

    def __str__(self):
        r"""Retorna uma ‘string’ com as informações do código QR.

        Método para exibir o texto do QR e a pasta onde está salvo.

        """
        return f'Texto: {self.texto}\nPasta: {self.imagem_caminho}'

    def __repr__(self) -> str:
        """Representação do objeto."""
        return (
            f'<{self.__class__.__name__}> {self.__class__.__doc__}\n'
            f'{self.__class__.__module__} {self.__dict__}'
        )


def main():
    """Função principal."""
    qr = QRCodeEncoderDecoder()
    qr.interface()


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
