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
from Conversores import Conversores
from decouple import config

from tests.loguru_conf import logger

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

API_KEY: Final[str] = config('SECRET_KEY')  # chave secreta no .env
URL: Final[str] = (
    f'http://api.openweathermap.org/data/2.5/weather?'
    f'&appid={API_KEY}&lang=pt_br&units=metric'
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
        """Obtém a data e hora em segundos unix, UTC.

        Unix é o número de segundos desde 1970-01-01 00:00:00 UTC.

        :return: data e hora em ano, mês, dia, hora, minuto e segundo.
        :rtype: datetime
        """
        return datetime.fromtimestamp(self.info['dt'])

    @property
    def velocidade_vento(self) -> float:
        """Obtém a velocidade do vento em m/s.

        :return: velocidade do vento em km/h.
        :rtype: float
        """
        return self.info['wind']['speed'] * 3.6  # m/s -> km/h

    @property
    def direcao_vento(self) -> str:
        """Obtém a direção do vento em graus.

        :return: direção do vento em direção cardinal.
        :rtype: str
        """
        return self.direcao_vento_cardinal(self.info['wind']['deg'])

    @property
    def rajada_vento(self) -> float:
        """Obtém a rajada do vento em m/s.

        :return: rajada do vento em km/h.
        :rtype: float
        """
        return self.info['wind']['gust'] * 3.6  # m/s -> km/h

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
        """Obtém o fuso horário em segundos unix, UTC.

        Unix timestamp é o número de segundos desde 1 de janeiro de 1970 até a
        data e hora especificada.

        :return: fuso horário em horas.
        :rtype: float
        """
        return (
            datetime.fromtimestamp(self.info['dt'])
            .astimezone()
            .utcoffset()
            .total_seconds()
            / 3600  # segundos -> horas
        )

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
        return self.info['visibility'] // 1000  # m -> km

    @property
    def por_do_sol(self) -> datetime:
        """Obtém a hora por do sol em segundos unix, UTC.

        :return: pôr do sol em ano, mês, dia, hora, minuto e segundo.
        :rtype: datetime
        """
        return datetime.fromtimestamp(self.info['sys']['sunset'])

    @property
    def nascer_do_sol(self) -> datetime:
        """Obtém a hora nascer do sol em segundos unix, UTC.

        :return: nascer do sol em ano, mês, dia, hora, minuto e segundo.
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
            f'Latitude: {self.latitude} | Longitude: {self.longitude} | '
            f'Fuso Horário: {self.fuso_horario}\n'
            f'{"-" * 61}\n'
            f'Descrição: {self.descricao}\n'
            f'Temperatura: {self.temperatura:.1f}ºC\n'
            f'\t máxima: {self.temperatura_maxima:.1f}ºC\n'
            f'\t mínima: {self.temperatura_minima:.1f}ºC\n'
            f'Pressão: {self.pressao:} hPa\n'
            f'Umidade: {self.umidade:} %\n'
            f'Vento: {self.velocidade_vento:.2f} km/h - '
            f'{self.direcao_vento}\n'
            f'\t rajada: {self.rajada_vento:.2f} km/h\n'
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


def main() -> None:
    """Função principal."""
    sunrise = InformacoesMeteorologicas('Montevideo')
    sunrise.obter_informacoes()
    print(sunrise.nascer_do_sol)
    print(sunrise.fuso_horario)
    data_london = InformacoesMeteorologicas('Londres')
    print(data_london.obter_informacoes())
    data_montevideo = InformacoesMeteorologicas('Montevideo')
    print(data_montevideo.obter_informacoes())
    data_sao_paulo = InformacoesMeteorologicas('São Paulo')
    print(data_sao_paulo.obter_informacoes())
    data_sao_jose_dos_campos = InformacoesMeteorologicas('São José dos Campos')
    print(data_sao_jose_dos_campos.obter_informacoes())


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
