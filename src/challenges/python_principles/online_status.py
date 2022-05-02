# -*- coding: utf-8 -*-
r"""online_status.py in: 2022-05-01.

Python version: 3.10.0

statuses = {
    'Alice': 'online',
    'Bob': 'offline',
    'Eve': 'online',
}

Função chamada online_count que leva um parâmetro. O parâmetro é um
dicionário que mapeia ‘strings’ de nomes e o estados dos usuários; 'online' ou
'offline', como visto acima.

Sua função deve retornar o número de pessoas que estão ‘online’.
"""
from tests.loguru_conf import logger


def online_count(statuses: dict) -> int:
    """Retorna o número de pessoas ‘online’.

    Explanação da 'list comprehension':
    https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

    online_users = []
    for name, status in statuses.items():
        if status == 'online':
            online_users.append(name)
    return len(online_users)

    :param statuses: dicionário de nomes e status
    :type statuses: dict
    :return: número de pessoas 'online'
    :rtype: int
    """
    return len(
        [name for name, status in statuses.items() if status == 'online']
    )


def main():
    """Main function."""
    statuses = {
        'Alice': 'online',
        'Bob': 'offline',
        'Eve': 'online',
    }

    print(online_count(statuses))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
