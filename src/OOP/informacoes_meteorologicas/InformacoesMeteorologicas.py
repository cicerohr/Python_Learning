# -*- coding: utf-8 -*-
r"""InformacoesMeteorologicas.py in: 2022-05-16.

Classe para informações meteorologicas. Inspirado no tutorial Code With Tomi

É utilizado a API do OpenWeatherMap para obter informações meteorologicas.
https://openweathermap.org/current#name

@author: Cícero
@link: https://www.youtube.com/watch?v=SqvVm3QiQVk&t=1494s
"""
import locale
from datetime import datetime
from typing import Final

import requests
from decouple import config
from unicodedata import normalize

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

API_KEY: Final[str] = config('SECRET_KEY')  # chave secreta no .env
URL: Final[str] = (
    f'http://api.openweathermap.org/data/2.5/weather?'
    f'&appid={API_KEY}&lang=pt_br&units=metric'
)


class Conversores:
    r"""Classe para conversões de dados.

    Conversor da direção do vento de graus para direção cardinal.

    Conversor de palavras acentuadas para palavras sem acentos.
    """

    @staticmethod
    def direcao_vento_cardinal(direcao_vento_graus: int) -> str:
        r"""Converte a direção do vento de graus para direção cardinal.

        :param direcao_vento_graus: direção do vento em graus.
        :type direcao_vento_graus: int.
        :return: direção do vento em direção cardinal.
        :rtype: str.
        """
        if 348.75 <= direcao_vento_graus <= 11.25:
            return 'Norte'
        if 11.25 <= direcao_vento_graus <= 33.75:
            return 'Nordeste'
        if 33.75 <= direcao_vento_graus <= 56.25:
            return 'Leste'
        if 56.25 <= direcao_vento_graus <= 78.75:
            return 'Sudeste'
        if 78.75 <= direcao_vento_graus <= 101.25:
            return 'Sul'
        if 101.25 <= direcao_vento_graus <= 123.75:
            return 'Sudoeste'
        if 123.75 <= direcao_vento_graus <= 146.25:
            return 'Oeste'
        if 146.25 <= direcao_vento_graus <= 168.75:
            return 'Noroeste'
        if 168.75 <= direcao_vento_graus <= 191.25:
            return 'Norte'
        if 191.25 <= direcao_vento_graus <= 213.75:
            return 'Nordeste'
        if 213.75 <= direcao_vento_graus <= 236.25:
            return 'Leste'
        if 236.25 <= direcao_vento_graus <= 258.75:
            return 'Sudeste'
        if 258.75 <= direcao_vento_graus <= 281.25:
            return 'Sul'
        if 281.25 <= direcao_vento_graus <= 303.75:
            return 'Sudoeste'
        if 303.75 <= direcao_vento_graus <= 326.25:
            return 'Oeste'
        if 326.25 <= direcao_vento_graus <= 348.75:
            return 'Noroeste'

    @staticmethod
    def palavra_acentuada_n_acentuada(palavra_acentuada: str) -> str:
        r"""Converte palavras acentuadas para palavras sem acentuação.

        :param palavra_acentuada: palavra com acento.
        :type palavra_acentuada: str.
        :return: palavra sem acento.
        :rtype: str.
        """
        return (
            normalize('NFKD', palavra_acentuada)
            .encode('ASCII', 'ignore')
            .decode('ASCII')
        )


class InformacoesMeteorologicas(Conversores):
    """Classe para obter informações meteorologicas.

    A classe utiliza a API do OpenWeatherMap para obter informações
    meteorologicas.
    """

    def __init__(self, cidade: str) -> None:
        """Inicializa as informações meteorologicas.

        :param cidade: cidade a ser pesquisada.
        :type cidade: str
        """
        super().__init__()
        self.cidade = self.palavra_acentuada_n_acentuada(cidade)
        self.info = self.obter_informacoes()

    def obter_informacoes(self) -> dict:
        """Obtém as informações meteorologicas da API.

        :return: informações meteorologicas.
        :rtype: dict
        """
        url = f'{URL}&q={self.cidade}'
        resposta = requests.get(url)
        return resposta.json()

    @property
    def temperatura(self) -> float:
        """Obtém a temperatura.

        :return: temperatura.
        :rtype: float
        """
        return self.info['main']['temp']

    @property
    def temperatura_maxima(self) -> float:
        """Obtém a temperatura máxima.

        :return: temperatura máxima.
        :rtype: float
        """
        return self.info['main']['temp_max']

    @property
    def temperatura_minima(self) -> float:
        """Obtém a temperatura mínima.

        :return: temperatura mínima.
        :rtype: float
        """
        return self.info['main']['temp_min']

    @property
    def pressao(self) -> int:
        """Obtém a pressão.

        :return: pressão.
        :rtype: int
        """
        return self.info['main']['pressure']

    @property
    def umidade(self) -> int:
        """Obtém a umidade.

        :return: umidade.
        :rtype: int
        """
        return self.info['main']['humidity']

    @property
    def descricao(self) -> str:
        """Obtém a descrição.

        :return: descrição.
        :rtype: str
        """
        return self.info['weather'][0]['description']

    @property
    def data_hora(self) -> datetime:
        """Obtém a data e hora.

        :return: data e hora.
        :rtype: datetime
        """
        return datetime.fromtimestamp(self.info['dt'])

    @property
    def velocidade_vento(self) -> float:
        """Obtém a velocidade do vento.

        :return: velocidade do vento.
        :rtype: float
        """
        return self.info['wind']['speed']

    @property
    def direcao_vento(self) -> str:
        """Obtém a direção do vento.

        :return: direção do vento.
        :rtype: str
        """
        return self.direcao_vento_cardinal(self.info['wind']['deg'])

    @property
    def rajada_vento(self) -> float:
        """Obtém a rajada do vento.

        :return: rajada do vento.
        :rtype: float
        """
        return self.info['wind']['gust']

    @property
    def nome(self) -> str:
        """Obtém o nome da cidade.

        :return: nome da cidade.
        :rtype: str
        """
        return self.info['name']

    @property
    def pais(self) -> str:
        """Obtém o nome do país.

        :return: nome do país.
        :rtype: str
        """
        return self.info['sys']['country']

    @property
    def fuso_horario(self) -> float:
        """Obtém o fuso horário.

        :return: fuso horário.
        :rtype: float
        """
        return datetime.fromtimestamp(self.info['dt']).astimezone().utcoffset().total_seconds() / 3600

    @property
    def latitude(self) -> float:
        """Obtém a latitude.

        :return: latitude.
        :rtype: float
        """
        return self.info['coord']['lat']

    @property
    def longitude(self) -> float:
        """Obtém a longitude.

        :return: longitude.
        :rtype: float
        """
        return self.info['coord']['lon']

    @property
    def visibilidade(self) -> int:
        """Obtém a visibilidade.

        :return: visibilidade.
        :rtype: int
        """
        return self.info['visibility'] // 1000

    @property
    def por_do_sol(self) -> datetime:
        """Obtém a hora por do sol.

        :return: por do sol.
        :rtype: datetime
        """
        return datetime.fromtimestamp(self.info['sys']['sunset'])

    @property
    def nascer_do_sol(self) -> datetime:
        """Obtém a hora nascer do sol.

        :return: nascer do sol.
        :rtype: datetime
        """
        return datetime.fromtimestamp(self.info['sys']['sunrise'])

    def __str__(self) -> str:
        """Retorna dados do objeto.

        :return: dados do objeto.
        :rtype: str
        """
        return (
            f' {self.nome}/{self.pais} - '
            f'{self.data_hora} '.center(61, '=') + '\n'
            f'Latitude: {self.latitude} | Longitude: {self.longitude} | Fuso Horário: {self.fuso_horario}\n'
            f'{"-" * 61}\n'
            f'Descrição: {self.descricao}\n'
            f'Temperatura: {self.temperatura:.1f}ºC\n'
            f'\t máxima: {self.temperatura_maxima:.1f}ºC\n'
            f'\t mínima: {self.temperatura_minima:.1f}ºC\n'
            f'Pressão: {self.pressao:} hPa\n'
            f'Umidade: {self.umidade:} %\n'
            f'Vento: {self.velocidade_vento:.2f} m/s - '
            f'{self.direcao_vento}\n'
            f'\t rajada: {self.rajada_vento:.2f} m/s\n'
            f'Visibilidade: {self.visibilidade} km\n'
            f'Nascer do sol: {self.nascer_do_sol.strftime("%H:%M")}\n'
            f'Pôr do sol: {self.por_do_sol.strftime("%H:%M")}\n'
        )

    def __repr__(self) -> str:
        """Representação do objeto."""
        return (
            f'{self.__class__.__name__}(cidade="{self.nome}")\n'
            f'{self.__class__.__doc__}\n'
            f'{self.__class__.__module__} {self.__dict__}\n'
        )
