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

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

API_KEY: Final[str] = config('SECRET_KEY')
URL = f'http://api.openweathermap.org/data/2.5/weather?&appid={API_KEY}&lang=pt_br&units=metric'


class InformacoesMeteorologicas:
    """Classe para informações meteorologicas."""

    def __init__(self, cidade: str) -> None:
        """Inicializa as informações meteorologicas.

        Args:
            cidade (str): Nome da cidade.

        :param cidade: cidade a ser pesquisada.
        :type cidade: str
        """
        self.__cidade = cidade
        # self.__api_key = config('SECRET_KEY')  # pega a chave secreta
        # self.__url_base = f'http://api.openweathermap.org/data/2.5/weather?q=
        # self.__url_final = (
        #     f'{self.__url_base}{self.__cidade}'
        #     f'&appid={API_KEY}&lang=pt_br&units=metric'
        # )
        self.__informacoes = self.__obter_informacoes()

    @property
    def cidade(self):
        """Retorna o nome da cidade."""
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        """Define o nome da cidade."""
        self.__cidade = cidade

    @property
    def pais(self):
        """Retorna o nome do pais."""
        return self.__informacoes['sys']['country']

    @property
    def latitude(self):
        """Retorna a latitude."""
        return self.__informacoes['coord']['lat']

    @property
    def longitude(self):
        """Retorna a longitude."""
        return self.__informacoes['coord']['lon']

    @property
    def temperatura(self):
        """Retorna a temperatura."""
        return self.__informacoes['main']['temp']

    @property
    def temperatura_maxima(self):
        """Retorna a temperatura maxima."""
        return self.__informacoes['main']['temp_max']

    @property
    def temperatura_minima(self):
        """Retorna a temperatura minima."""
        return self.__informacoes['main']['temp_min']

    @property
    def pressao(self):
        """Retorna a pressao."""
        return self.__informacoes['main']['pressure']

    @property
    def umidade(self):
        """Retorna a umidade."""
        return self.__informacoes['main']['humidity']

    @property
    def visibilidade(self):
        """Retorna a visibilidade."""
        return self.__informacoes['visibility']

    @property
    def vento(self):
        """Retorna a velocidade do vento."""
        return self.__informacoes['wind']['speed']

    @property
    def direcao_vento(self):
        """Retorna a direcao do vento."""
        return self.__informacoes['wind']['deg']

    @property
    def condicao(self):
        """Retorna a condicao."""
        return self.__informacoes['weather'][0]['description']

    @property
    def data(self):
        """Retorna a data."""
        return datetime.fromtimestamp(int(self.__informacoes['dt']))

    def __obter_informacoes(self) -> dict:
        """Obtem as informações meteorologicas.

        :return: json com as informações meteorologicas.
        :rtype: dict
        """
        url = f'{URL}&q={self.cidade}'
        response = requests.get(url)
        return response.json()

    def converter_direcao_vento_abreviatura(self) -> str:
        """Converte a direcao do vento para abreviatura.

        :return: abreviatura da direcao do vento.
        :rtype: str
        """
        if 348.75 <= self.direcao_vento <= 11.25:
            return 'N'
        if 11.25 <= self.direcao_vento <= 33.75:
            return 'NNE'
        if 33.75 <= self.direcao_vento <= 56.25:
            return 'NE'
        if 56.25 <= self.direcao_vento <= 78.75:
            return 'ENE'
        if 78.75 <= self.direcao_vento <= 101.25:
            return 'E'
        if 101.25 <= self.direcao_vento <= 123.75:
            return 'ESE'
        if 123.75 <= self.direcao_vento <= 146.25:
            return 'SE'
        if 146.25 <= self.direcao_vento <= 168.75:
            return 'SSE'
        if 168.75 <= self.direcao_vento <= 191.25:
            return 'S'
        if 191.25 <= self.direcao_vento <= 213.75:
            return 'SSW'
        if 213.75 <= self.direcao_vento <= 236.25:
            return 'SW'
        if 236.25 <= self.direcao_vento <= 258.75:
            return 'WSW'
        if 258.75 <= self.direcao_vento <= 281.25:
            return 'W'
        if 281.25 <= self.direcao_vento <= 303.75:
            return 'WNW'
        if 303.75 <= self.direcao_vento <= 326.25:
            return 'NW'
        if 326.25 <= self.direcao_vento <= 348.75:
            return 'NNW'

    def __str__(self) -> str:
        """Retorna a representação em ‘string’."""
        return (
                f' {self.cidade}/{self.pais} - {self.data.strftime("%d/%m/%Y")} às {self.data.strftime("%H:%M")} '.center(50, '=') + '\n'
                f'Latitude: {locale.format_string("%.4f", self.latitude)}\n'
                f'Longitude: {locale.format_string("%.4f", self.longitude)}\n'
                f'Condição: {self.condicao}\n'
                f'Temperatura: '
                f'{locale.format_string("%.2f", self.temperatura)} °C\n'
                f'Temperatura maxima: '
                f'{locale.format_string("%.2f", self.temperatura_maxima)} °C\n'
                f'Temperatura minima: '
                f'{locale.format_string("%.2f", self.temperatura_minima)} °C\n'
                f'Pressão: {self.pressao} hPa\n'
                f'Umidade: {self.umidade} %\n'
                f'Visibilidade: '
                f'{locale.format_string("%.0f", self.visibilidade / 1000)} km\n'
                f'Vento: {locale.format_string("%.2f", self.vento)} m/s\n'
                f'Direção do vento: {self.direcao_vento}°'
                f' - {self.converter_direcao_vento_abreviatura()}\n '
        )

    def __repr__(self) -> str:
        """Representação do objeto."""
        return (
            f'{self.__class__.__name__}("{self.cidade}")\n'
            f'{self.__class__.__doc__}\n'
            f'{self.__class__.__module__} {self.__dict__}\n'
        )
