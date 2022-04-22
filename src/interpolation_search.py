# -*- coding: utf-8 -*-
"""interpolation_search.py in: 2022-04-10.

Python version: 3.10.0

Interpolation search is an algorithm for finding an element in a sorted array.
It works by first finding the two elements in the array that surround the
element we are looking for. Then, we calculate
the position of the element we are looking for in relation to those
two elements. If the position is greater than the
first element and less than the second element, then we know that the element
must be in the array. Otherwise,
we know that the element is not in the array.

Source: https://en.wikipedia.org/wiki/Interpolation_search
"""


def interpolation_search(array, element):
    """-> Interpolation search.

    Complexity of algorithm: O(log log n).

    :param array: Array to search in.
    :param element: Element to search for.
    :return: Index of element in array.
    """
    low = 0
    high = len(array) - 1
    while low <= high and array[low] <= element <= array[high]:
        position = low + (
            (element - array[low]) * (high - low) // (array[high] - array[low])
        )
        if array[position] == element:
            return position
        if array[position] < element:
            low = position + 1
        else:
            high = position - 1
    return -1


def main():
    """-> Main function."""
    array = [1, 2, 2, 4, 10, 12, 23, 32, 34, 45, 45, 67, 67]
    print(interpolation_search(array, 45))
    print(interpolation_search(array, 2))
    print(interpolation_search(array, 63))


if __name__ == '__main__':
    main()
