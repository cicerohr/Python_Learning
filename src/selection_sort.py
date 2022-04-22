# -*- coding: utf-8 -*-
"""selection_sort.py in: 2022-04-08.

Sort Selection Algorithm (Ordenação por Seleção).

Fonte:
https://www.youtube.com/watch?v=dFd6us_xFSc&list=PLvS2JoIlSA4AiEnL_tWkFFWpWfiGqzX83&index=2
"""

from logs.loguru_conf import logger


def selection_sort(lista: list) -> list:
    """-> Selection Sort Algorithm.

    Complexity of algorithm: O(n²)
    Comparisons: (n -1) + (n - 2) + ... + 1 = (n² - n)/2
    Swap: n - 1

    :param lista: list of elements to be sorted
    :return: list sorted
    :rtype: list

    Tests:
    >>> selection_sort([5, 3, 6, 2, 10])
    [2, 3, 5, 6, 10]
    >>> selection_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> selection_sort([5])
    [5]
    >>> selection_sort(['A', 'B', 'C', 'D', 'E'])
    ['A', 'B', 'C', 'D', 'E']
    >>> selection_sort(['C', 'B', 'A'])
    ['A', 'B', 'C']
    >>> selection_sort(['A'])
    ['A']
    >>> selection_sort(['Walter', 'Elaine', 'Michael', 'Gustavo', 'Diane'])
    ['Diane', 'Elaine', 'Gustavo', 'Michael', 'Walter']
    >>> selection_sort(['Diane', 'Michael', 'Elaine', 'Gustavo', 'Walter'])
    ['Diane', 'Elaine', 'Gustavo', 'Michael', 'Walter']
    >>> selection_sort([])
    []
    """
    for i, _ in enumerate(lista):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
        logger.debug(f'{i}: {lista}')
    return lista


def main():
    """Main function."""
    print(selection_sort([5, 3, 6, 2, 10]))
    print(selection_sort([1, 2, 3, 4, 5]))
    print(selection_sort([5]))
    print(selection_sort(['A', 'B', 'C', 'D', 'E']))
    print(selection_sort(['C', 'B', 'A']))
    print(selection_sort(['A']))
    print(selection_sort(['Walter', 'Elaine', 'Michael', 'Gustavo', 'Diane']))
    print(selection_sort(['Diane', 'Michael', 'Elaine', 'Gustavo', 'Walter']))
    print(selection_sort([]))


if __name__ == '__main__':
    logger.info('Program  started.')
    main()
    logger.info('Program ended.')
