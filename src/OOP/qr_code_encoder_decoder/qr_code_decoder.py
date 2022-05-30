# -*- coding: utf-8 -*-
r"""qr_code_decoder.py in: 2022-05-29.

@author: Cícero
"""
from pathlib import Path

from PIL import Image
from pyzbar.pyzbar import decode

from tests.loguru_conf import logger
from utilitarios import Utilitarios as Util


class QRCodeDecoder(Util):
    """Classe para descodificar um código QR."""

    def __init__(self, caminho_imagem: str) -> None:
        """Construtor da classe.

        :param caminho_imagem: caminho absoluto da imagem.
        :type caminho_imagem: str
        """
        super().__init__()
        self.caminho_imagem = caminho_imagem
        self.imagem = None
        self.dados = None

    def descodificar_qr_code(self) -> tuple:
        """Descodifica o código QR.

        :return: tupla com o estado da operação e mensagem de erro.
        :rtype: tuple
        """
        if Path(self.caminho_imagem).exists():
            try:
                self.imagem = Image.open(self.caminho_imagem)
                self.dados = decode(self.imagem)[0].data.decode('utf-8')
            except Exception as e:
                msg1 = f'Erro ao decodificar o código QR: {e}'
                logger.error(msg1)
                return False, msg1
        else:
            msg2 = f'Erro! O caminho não existe: {self.caminho_imagem}'
            logger.error(f'Arquivo {msg2}')
            return False, msg2
        return True, '_Ok!'

    def __str__(self) -> str:
        """Retorna o código QR ou a mensagem de erro."""
        if self.descodificar_qr_code()[0]:
            return self.dados
        return f'{self.descodificar_qr_code()[1]}'


def main():
    """Função principal."""
    print(QRCodeDecoder(f'{Util.caminho_relativo_assets()}/teste.png'))
    print(repr(QRCodeDecoder(f'{Util.caminho_relativo_assets()}/teste.png')))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
