# -*- coding: utf-8 -*-
"""sorted_list_search.py in: 2022-04-08.

Python version: 3.10.0

Comparison between search algorithms in ordered lists.
"""
import timeit

from logs.loguru_conf import logger


def linear_search(array: list, value: int | str) -> int:
    """-> Linear search algorithm.

    It compares each element to the value that we are looking for.
    If both match, the element is found, and the algorithm returns the
    index position of the key.

    Complexity of algorithm: O(n)

    :param array: list to search in.
    :param value: value to search for.
    :return: index of value in array if found, -1 otherwise.

    Tests:
    >>> linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
    9
    >>> linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)
    -1
    >>> linear_search(['A', 'C', 'D', 'E'], 'E')
    3
    >>> linear_search(['A', 'C', 'D', 'E'], 'F')
    -1
    >>> linear_search([10], 10)
    0
    """
    for i, _ in enumerate(array):
        if array[i] == value:
            return i
    return -1


def binary_search(array: list, value: int | str) -> int:
    """-> Binary search algorithm.

    It is a search algorithm that works by comparing the value of the middle
    element of the sorted array with the value to be searched. If the value is
    greater, then the search continues in the right half of the array, and
    if the value is less, then the search continues in the left half of
    the array.

    Complexity of algorithm: O(log n)

    :param array: list to search in.
    :param value: value to search for.
    :return: index of value in list if found, -1 otherwise.

    Tests:
    >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
    9
    >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)
    -1
    >>> binary_search(['A', 'C', 'D', 'E'], 'E')
    3
    >>> binary_search(['A', 'C', 'D', 'E'], 'F')
    -1
    >>> binary_search([10], 10)
    0
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == value:
            return mid
        if array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def interpolation_search(array: list, value: int | str) -> int:
    """-> Interpolation search.

    It is an algorithm for finding an element in a sorted array.
    It works by first finding the two elements in the array that surround the
    element we are looking for. Then, we calculate the position of the element
    we are looking for in relation to those two elements. If the position is
    greater than the first element and less than the second element, then we
    know that the element must be in the array. Otherwise, we know that the
    element is not in the array.

    Source: https://en.wikipedia.org/wiki/Interpolation_search

    Complexity of algorithm: O(log(log n)).

    Tests:
    >>> interpolation_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
    9
    >>> interpolation_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
    0
    >>> interpolation_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)
    -1
    >>> interpolation_search([2], 2)
    0

    :param array: list to search in.
    :param value: value to search for.
    :return: index of value in list if found, -1 if not found.
    """
    low = 0
    high = len(array) - 1

    while low <= high and array[low] <= value <= array[high]:
        if low == high:
            if array[low] == value:
                logger.debug(f'List contains one element. {array}')
                return low
            return -1
        index = low + (
            (value - array[low]) * (high - low) // (array[high] - array[low])
        )
        if array[index] == value:
            return index
        if array[index] < value:
            low = index + 1
        else:
            high = index - 1
    return -1


def main():
    """-> Main function.

    Shows the running time of linear search, binary search and interpolation
    search algorithms.
    """
    totais = [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]

    for total in totais:
        array = list(range(total))
        value = total - 1
        print(f'\nTotal of elements: {total:_}')

        start = timeit.default_timer()
        linear_search(array, value)
        end = timeit.default_timer()
        print(f'\tlinear search:\t\t\t{end - start} s')

        start = timeit.default_timer()
        binary_search(array, value)
        end = timeit.default_timer()
        print(f'\tBinary search:\t\t\t{end - start} s')

        start = timeit.default_timer()
        interpolation_search(array, value)
        end = timeit.default_timer()
        print(f'\tInterpolation search:\t{end - start} s')


if __name__ == '__main__':
    main()
