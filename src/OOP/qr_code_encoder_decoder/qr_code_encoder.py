# -*- coding: utf-8 -*-
r"""qr_code_encoder.py in: 2022-05-29.

@author: Cícero
"""
import qrcode

from tests.loguru_conf import logger
from utilitarios import Utilitarios as Util


class QRCodeEncoder(Util):
    """Classe para codificação de códigos QR."""

    def __init__(self, texto: str) -> None:
        """Construtor da classe.

        :param texto: texto a ser codificado.
        :type texto: str
        """
        super().__init__()
        self.texto = texto
        self.qr_code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        self.caminho_nome_arquivo_qr_code = (
            f'{Util.caminho_relativo_assets()}/'
            f'{Util.gerar_nome_arquivo_qr_code()}'
        )
        self.gerar_qr_code()

    def gerar_qr_code(self) -> None:
        """Gera o código QR a partir de um texto."""
        self.qr_code.add_data(self.texto)
        self.qr_code.make(fit=True)
        img = self.qr_code.make_image(fill_color='black', back_color='white')
        img.save(self.caminho_nome_arquivo_qr_code)

    def __str__(self) -> str:
        """Retorna uma ‘string’ com o caminho e o nome do arquivo."""
        return self.caminho_nome_arquivo_qr_code


def main():
    """Função principal."""
    print(QRCodeEncoder('teste'))
    print(repr(QRCodeEncoder('teste')))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
