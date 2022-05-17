# -*- coding: utf-8 -*-
r"""informacoes_meteorologicas.py in: 2022-05-15.

Neste tutorial Code With Tomi, você aprenderá como construir um programa que
coleta dados do usuário em um local específico e gera os detalhes climáticos
desse local fornecido.

Este é um ótimo projeto para começar a aprender como obter dados de APIs.

@author: Tomi Tokko
@modified by: Cícero
@link: https://www.youtube.com/watch?v=SqvVm3QiQVk&t=1494s
"""
from pprint import pprint
import requests
from decouple import config

from tests.loguru_conf import logger


def main():
    """Função principal."""
    # Obtém a chave da API do OpenWeatherMap no arquivo '.env'.
    API_KEY = config('SECRET_KEY')

    cidade = input('Digite o nome da cidade: ')
    url_base = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}' \
               f'&appid={API_KEY}&lang=pt_br&units=metric'

    info_meteorologicas = requests.get(url_base).json()

    url_icon = f'http://openweathermap.org/img/wn/' \
               f'{info_meteorologicas["weather"][0]["icon"]}@2x.png'

    pprint(info_meteorologicas)
    print(f'\nCidade: {info_meteorologicas["name"]}')
    print(f'Temperatura: {info_meteorologicas["main"]["temp"]} °C')
    print(f'Temperatura máxima: {info_meteorologicas["main"]["temp_max"]} °C')
    print(f'Temperatura mínima: {info_meteorologicas["main"]["temp_min"]} °C')
    print(f'Pressão: {info_meteorologicas["main"]["pressure"]} hPa')
    print(f'Humidade: {info_meteorologicas["main"]["humidity"]} %')
    print(f'Visibilidade: {info_meteorologicas["visibility"] / 1000} km')
    print(f'Velocidade do vento: {info_meteorologicas["wind"]["speed"]} m/s')
    print(f'Rajadas de vento: {info_meteorologicas["wind"]["gust"]} m/s')
    print(f'Direção do vento: {info_meteorologicas["wind"]["deg"]}°')
    print(f'Amanhece às {info_meteorologicas["sys"]["sunrise"]}')
    print(f'Por do sol às {info_meteorologicas["sys"]["sunset"]}')
    print(f'Ícone: {url_icon}')


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
