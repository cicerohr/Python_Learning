# Studies

The objective of this project is to create programs for learning the Python
programming language, as well as the use of libraries to improve the
performance of algorithms.

## Contents

* Sorted List Search
    * [Linear search algorithm.](#linear-search-algorithm)
    * [Binary search algorithm.](#binary-search-algorithm)
    * [Interpolation search algorithm.](#interpolation-search-algorithm)
* Selection Sort
    * [Selection sort algorithm.](#selection-sort-algorithm)

## [Sorted List Search](../src/sorted_list_search.py)

### Linear search algorithm.

It compares each element to the value that we are looking for. If both match,
the element is found, and the algorithm returns the index position of the key.

Code:

    for i, _ in enumerate(array):
        if array[i] == value:
            return i
    return -1

### Binary search algorithm.

We start with a hunch of where the wanted element might be. Our guess is always
to choose the middle element of the arrangement. If this guess is right, the
search ends because we find the search element. If the guess is wrong, we can
restrict our next guess to a specific part of the arrangement, given that it is
ordered. The reasoning behind this is that if the element sought is greater
than the middle element of the arrangement, we know that the element sought can
only be in the second half of the arrangement. Otherwise, the searched element
can only be in the first half of the arrangement.

Code:

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

### Interpolation search algorithm.

Interpolation search calculates the probable position of the element we are
searching for using the formula:

    index = low + [(value - array[low]) * (high-low) / (array[high] - array[low])]

Where the variables are:

* **array**: list of elements to be searched.
* **value**: the element we are searching for.

* **index**: the probable index of the search element.
  This is computed to be a higher value when value is closer in
  value to the element at the end of the array (array[high]), and
  lower when value is closer in value to the element at the start of
  the array (array[low]).
* **low**: the starting index of the array.
* **high**: the last index of the array.

The algorithm searches by calculating the value of index:

* If a match is found (when array[index] == value), the index is returned.
* If the value is less than array[index], the value for the index is
  re-calculated using the formula for the left sub-array.
* If the value is greater than array[index], the value for the index
  is re-calculated using the formula for the right sub-array.

Code:

    low = 0
    high = len(array) - 1

    while low <= high and array[low] <= value <= array[high]:
        if low == high:
            if array[low] == value:
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

## [Selection Sort](../src/selection_sort.py)

### Selection sort algorithm.

The selection sort algorithm has O(n²) time complexity, due to which it becomes
less effective on large lists, usually performs worse than the similar
insertion sort.

Code:

    for i, _ in enumerate(the_list):
        minimum = i
        for j in range(i + 1, len(the_list)):
            if the_list[j] < the_list[minimum]:
                minimum = j
        the_list[i], the_list[minimum] = the_list[minimum], the_list[i]
    return the_list
