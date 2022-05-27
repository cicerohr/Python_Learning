# -*- coding: utf-8 -*-
r"""InformacoesMeteorologicas.py in: 2022-05-16.

Classe para informações meteorologicas. Inspirado no tutorial Code With Tomi

É utilizado a API do OpenWeatherMap para obter informações meteorologicas.
https://openweathermap.org/current#name

@author: Cícero
@link: https://www.youtube.com/watch?v=SqvVm3QiQVk&t=1494s
"""
from datetime import datetime, timedelta, timezone
from typing import Final

import requests
from decouple import config

from Conversores import Conversores
from tests.loguru_conf import logger

API_KEY: Final[str] = config('SECRET_KEY')  # chave secreta no .env


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
        self.cidade = self.retirar_acento(cidade)
        self.info = self.obter_informacoes()

    def obter_informacoes(self) -> dict:
        """Obtém as informações meteorologicas da API.

        :return: informações meteorologicas.
        :rtype: dict
        """
        url = 'https://api.openweathermap.org/data/2.5/weather'
        parametros = {
            'q': self.cidade,
            'appid': API_KEY,
            'lang': 'pt_br',
            'units': 'metric',
        }
        try:
            resposta = requests.get(url, params=parametros)
            return resposta.json()
        except Exception as e:
            logger.error(e)
            return {}

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
    def nebulosidade(self) -> int:
        """Obtém a nebulosidade.

        :return: nebulosidade.
        :rtype: int
        """
        return self.info['clouds']['all']

    @property
    def descricao(self) -> str:
        """Obtém a descrição.

        :return: descrição.
        :rtype: str
        """
        return self.info['weather'][0]['description']

    @property
    def icone(self) -> str:
        """Obtém o icone.

        :return: icone.
        :rtype: str
        """
        return self.info['weather'][0]['icon']

    @property
    def sensacao_termica(self) -> float:
        """Obtém a sensação térmica.

        :return: sensação térmica.
        :rtype: float
        """
        return self.info['main']['feels_like']

    @property
    def data_hora(self) -> str:
        """Obtém a data e hora em segundos unix, UTC.

        Unix é o número de segundos a partir de: 1970-01-01 00:00:00 UTC.

        :return: data e hora em ano, mês, dia, hora, minuto e segundo.
        :rtype: str
        """
        return datetime.now(
            timezone(timedelta(hours=(self.info['timezone'] / 3600)))
        ).strftime('%Y-%m-%d %H:%M')

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
        return self.direcao_cardinal(self.info['wind']['deg'])

    @property
    def rajada_vento(self) -> float:
        """Obtém a rajada do vento em m/s.

        :return: rajada do vento em km/h.
        :rtype: float
        """
        try:
            return self.info['wind']['gust'] * 3.6  # m/s -> km/h
        except KeyError:
            return 0

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
    def fuso_horario(self) -> str:
        """Obtém o fuso horário em segundos unix, UTC.

        Unix timestamp é o número de segundos desde 1 de janeiro de 1970 até a
        data e hora especificada.

        :return: fuso horário em horas.
        :rtype: str
        """
        return datetime.now(
            timezone(timedelta(hours=(self.info['timezone'] / 3600)))
        ).strftime('%z')[:-2]

    @fuso_horario.setter
    def fuso_horario(self, fuso_horario):
        """Define o fuso horário.

        :param fuso_horario: fuso horário em horas.
        :type fuso_horario: float
        """
        self.fuso_horario = fuso_horario

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
    def nascer_do_sol(self) -> datetime:
        """Obtém a hora nascer do sol em segundos unix, UTC.

        :return: nascer do sol em ano, mês, dia, hora, minuto e segundo.
        :rtype: datetime
        """
        return datetime.fromtimestamp(
            self.info['sys']['sunrise'] + self.info['timezone'],
            tz=timezone.utc,
        )

    @property
    def por_do_sol(self) -> datetime:
        """Obtém a hora por do sol em segundos unix, UTC.

        :return: pôr do sol em ano, mês, dia, hora, minuto e segundo.
        :rtype: datetime
        """
        return datetime.fromtimestamp(
            self.info['sys']['sunset'] + self.info['timezone'], tz=timezone.utc
        )

    def __dict__(self):
        try:
            dict_ = {
                'nome': self.nome,
                'pais': self.pais,
                'data_hora': self.data_hora,
                'latitude': self.latitude,
                'longitude': self.longitude,
                'fuso_horario': self.fuso_horario,
                'temperatura': f'{self.temperatura:.1f}',
                'descricao': f'{self.descricao}',
                'icone': self.icone,
                'minima': f'{self.temperatura_minima:.1f}',
                'maxima': f'{self.temperatura_maxima:.1f}',
                'sensacao_termica': self.sensacao_termica,
                'pressao': self.pressao,
                'umidade': self.umidade,
                'nebulosidade': self.nebulosidade,
                'vento': f'{self.velocidade_vento:.2f}',
                'direcao_vento': self.direcao_vento,
                'rajada_vento': f'{self.rajada_vento:.2f}',
                'visibilidade': self.visibilidade,
                'nascer_do_sol': self.nascer_do_sol.strftime('%H:%M'),
                'por_do_sol': self.por_do_sol.strftime('%H:%M'),
            }
            return dict_
        except Exception as e:
            logger.error(f'Erro ao converter o objeto para dicionário: {e}')
            return -1

    def __str__(self) -> str | dict:
        """Retorna dados do objeto.

        :return: dados do objeto.
        :rtype: str | dict
        """
        try:
            string_retorno = f"""
            \t\t{self.nome}/{self.pais} | {self.data_hora}
            Lat.: {self.latitude} | Long.: {self.longitude} | 
            Fuso Horário: {self.fuso_horario}\n
            Descrição: {self.descricao}
            Temperatura: {self.temperatura:.2f}ºC
            \t máxima: {self.temperatura_maxima:.2f}ºC
            \t mínima: {self.temperatura_minima:.2f}ºC
            Pressão: {self.pressao:} hPa
            Umidade: {self.umidade:} %
            Vento: {self.velocidade_vento:.2f} km/h - {self.direcao_vento}
            \trajada: {self.rajada_vento:.2f} km/h
            Visibilidade: {self.visibilidade} km
            Nascer do sol: {self.nascer_do_sol.strftime("%H:%M")}
            Pôr do sol: {self.por_do_sol.strftime("%H:%M")}"""
            return string_retorno
        except KeyError as e:
            logger.error(f'Erro ao obter dados do objeto: {e}')
            return (
                f'Erro ao obter dados.\n\n'
                f'A cidade "{self.cidade}" está correta?'
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
    montevideo = InformacoesMeteorologicas('Montevideo')
    print(
        datetime.now(
            timezone(timedelta(hours=(montevideo.info['timezone'] / 3600)))
        ).strftime('%z')[:-2]
    )
    print(
        datetime.now(
            timezone(timedelta(hours=(montevideo.info['timezone'] / 3600)))
        )
    )
    # print(montevideo.obter_informacoes())
    # print(montevideo)
    print(montevideo.__dict__())


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
