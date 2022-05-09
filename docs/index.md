# Studies

The objective of this project is to create programs for learning the Python
programming language, as well as the use of libraries to improve the
performance of algorithms.

## Contents

* Sorted List Search
    * [Linear search algorithm.](#linear-search-algorithm)
    * [Binary search algorithm.](#binary-search-algorithm)
    * [Interpolation search algorithm.](#interpolation-search-algorithm)
    * [Algorithms performance test.](#algorithms-performance-test)
* Selection Sort
    * [Selection sort algorithm.](#selection-sort-algorithm)

* Game theory
    * [Minimax algorithm.](#minimax-algorithm)

* Pattern Matching
    * [Pattern matching statement.](#pattern-matching-statement)
* Challenges
   * [Challenges Folder](../src/challenges)

## [Sorted List Search](../src/sorted_list_search.py)

### Linear search algorithm.

It compares each element to the value that we are looking for. If both match,
the element is found, and the algorithm returns the index position of the key.

Code:

    for i, _ in enumerate(array):
        if array[i] == value:
            return i
    return -1

[🔝](#studies)

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

[🔝](#studies)

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

[🔝](#studies)

### Algorithms performance test.
Code:

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

Results:

    Total of elements: 100
        linear search:		8.500064723193645e-06 s
        Binary search:		3.100023604929447e-06 s
        Interpolation search:	1.9000144675374031e-06 s
    
    Total of elements: 1_000
        linear search:		5.91999851167202e-05 s
        Binary search:		2.800021320581436e-06 s
        Interpolation search:	1.400010660290718e-06 s
    
    Total of elements: 10_000
        linear search:		0.0005997000262141228 s
        Binary search:		3.100023604929447e-06 s
        Interpolation search:	1.200009137392044e-06 s
    
    Total of elements: 100_000
        linear search:		0.006108399946242571 s
        Binary search:		3.6999117583036423e-06 s
        Interpolation search:	1.400010660290718e-06 s
    
    Total of elements: 1_000_000
        linear search:		0.06024770007934421 s
        Binary search:		7.200054824352264e-06 s
        Interpolation search:	2.600019797682762e-06 s
    
    Total of elements: 10_000_000
        linear search:		0.7200529000256211 s
        Binary search:		1.8299906514585018e-05 s
        Interpolation search:	2.800021320581436e-06 s
    
    Total of elements: 100_000_000
        linear search:		11.250430999905802 s
        Binary search:		0.0008574000094085932 s
        Interpolation search:	0.00018770003225654364 s
    
    Process finished with exit code 0

[🔝](#studies)

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

[🔝](#studies)

## Game theory

### [Minimax algorithm.](../src/minimax.py)


[🔝](#studies)

## [Pattern matching statement](../src/pattern_matching.py)

The primary outcome of pattern matching is success or failure. In case of 
success we may say “the pattern succeeds”, “the match succeeds”, or 
“the pattern matches the subject value”.

In many cases a pattern contains subpatterns, and success or failure is 
determined by the success or failure of matching those subpatterns against the 
value (e.g., for OR patterns) or against parts of the value 
(e.g., for sequence patterns). This process typically processes the subpatterns 
from left to right until the overall outcome is determined. 
E.g., an OR pattern succeeds at the first succeeding subpattern, while a 
sequence patterns fails at the first failing subpattern.

A secondary outcome of pattern matching may be one or more name bindings. We 
may say “the pattern binds a value to a name”. When subpatterns tried until 
the first success, only the bindings due to the successful subpattern 
are valid; when trying until the first failure, the bindings are merged. 
Several more rules, explained below, apply to these cases. 
(See [PEP 634](https://peps.python.org/pep-0634/) for more details.)

<p align="center">
<a href="#pattern-matching-with-literals">Pattern matching with literals</a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="#pattern-matching-with-collections">Pattern matching with collections</a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="#naming-elements-in-pattern-matching">Naming elements in pattern matching</a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="#guard-pattern-matching">Guard pattern matching</a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="#irrefutable-case-blocks">Irrefutable case blocks</a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="#matching-patterns-in-classes">Matching patterns in classes</a>&nbsp;&nbsp;&nbsp;&nbsp;

### Pattern matching with literals
Code:

    def pattern_matching_switch_case(value):
    """Pattern matching used as switch case (literal)."""

        match value:
            case 1:
                print(1)
            case 2:
                print(2)
            case 3:
                print(3)
            case _:  # default
                print('different from 1, 2 and 3')
    
    print(' Pattern matching with literals '.center(80, '-').title())
    pattern_matching_switch_case(1)
    pattern_matching_switch_case(2)
    pattern_matching_switch_case(3)
    pattern_matching_switch_case(4)

Result:

    ------------------------ Pattern Matching With Literals ------------------------
    1
    2
    3
    different from 1, 2 and 3

[🔝](#pattern-matching-statement)

### Pattern matching with collections
code:

    def pattern_matching_not_literal(collection_values):
        """Pattern matching not literal."""

        match collection_values:
            case [1, 2, 3]:
                print(collection_values, f':pattern: [1, 2, 3]')
                print('collection of 3 elements with 1, 2 and 3; in this order',
                      end='\n\n')
            case [1, _, _]:  # _ is a wildcard
                print(collection_values, f':pattern: [1, _, _]')
                print('1 has to be the first element of the collection, '
                      'other elements can be anything', end='\n\n')
            case [_, 2, _]:
                print(collection_values, f':pattern: [_, 2, _]')
                print('2 must be the second element of the collection, '
                      'other elements can be anything', end='\n\n')
            case [] | [_]:  # | is the union operator
                print(collection_values, f':pattern: [] | [_]')
                print('empty collection or collection with one element',
                      end='\n\n')
            case [5 | 6, _, _]:  # | is the union operator
                print(collection_values, f':pattern: [5 | 6, _, _]')
                print('5 or 6 must be the first element of the collection, '
                      'other elements can be anything', end='\n\n')
            case [1, 2]:
                print(collection_values, f':pattern: [1, 2]')
                print('collection with elements 1 and 2, in that order',
                      end='\n\n')
            case [1, *_]:  # * is the splat operator
                print(collection_values, f':pattern: [1, *_]')
                print('collection with first element 1 and '
                      'any other element(s)', end='\n\n')
            case (7, *rest):  # * is the splat operator
                print(collection_values, f':pattern: (7, *rest)')
                print(f'collection with the first element 7 and '
                      f'the rest of the elements {rest=}', end='\n\n')
            case _:  # default
                print(collection_values)
                print('collection does not match pattern', end='\n\n')
    
    print(' Pattern matching with collections '.center(80, '-').title())
    pattern_matching_not_literal([4, 5, 6])
    pattern_matching_not_literal([1, 2, 3])
    pattern_matching_not_literal([1, 2, 4])
    pattern_matching_not_literal([3, 2, 1])
    pattern_matching_not_literal([])
    pattern_matching_not_literal([1])
    pattern_matching_not_literal([5, 9, 6])
    pattern_matching_not_literal([6, 9, 6])
    pattern_matching_not_literal([1, 2])
    pattern_matching_not_literal([1, 2, 3, 4])
    pattern_matching_not_literal((7, 8, 9, 10))

Result:

    ---------------------- Pattern Matching With Collections -----------------------
    [4, 5, 6]
    collection does not match pattern
    
    [1, 2, 3] :pattern: [1, 2, 3]
    collection of 3 elements with 1, 2 and 3; in this order
    
    [1, 2, 4] :pattern: [1, _, _]
    1 has to be the first element of the collection, other elements can be anything
    
    [3, 2, 1] :pattern: [_, 2, _]
    2 must be the second element of the collection, other elements can be anything
    
    [] :pattern: [] | [_]
    empty collection or collection with one element
    
    [1] :pattern: [] | [_]
    empty collection or collection with one element
    
    [5, 9, 6] :pattern: [5 | 6, _, _]
    5 or 6 must be the first element of the collection, other elements can be anything
    
    [6, 9, 6] :pattern: [5 | 6, _, _]
    5 or 6 must be the first element of the collection, other elements can be anything
    
    [1, 2] :pattern: [1, 2]
    collection with elements 1 and 2, in that order
    
    [1, 2, 3, 4] :pattern: [1, *_]
    collection with first element 1 and any other element(s)
    
    (7, 8, 9, 10) :pattern: (7, *rest)
    collection with the first element 7 and the rest of the elements rest=[8, 9, 10]

[🔝](#pattern-matching-statement)

### Naming elements in pattern matching
Code:

    def naming_elements_in_pattern_matching(color):
        """Naming each element of a collection."""

        match color:
            case r, g, b:
                print(f'r={r}, g={g}, b={b}', end='\n\n')
            case r, g, b, a:
                print(f'r={r}, g={g}, b={b}, a={a}', end='\n\n')
            case r, g, b, a, _:  # _ is a wildcard
                print(f'r={r}, g={g}, b={b}, a={a}', end='\n\n')
            case c, m, y, k:
                print(f'c={c}, m={m}, y={y}, k={k}', end='\n\n')

    print(' Naming elements in pattern matching '.center(80, '-').title())
    naming_elements_in_pattern_matching((255, 255, 255))
    naming_elements_in_pattern_matching((255, 255, 255, 255))
    naming_elements_in_pattern_matching((255, 255, 255, 255, 255))
    naming_elements_in_pattern_matching((255, 255, 255, 255, 255, 255))
    
Result:

    --------------------- Naming Elements In Pattern Matching ----------------------
    r=255, g=255, b=255
    
    r=255, g=255, b=255, a=255
    
    r=255, g=255, b=255, a=255    

[🔝](#pattern-matching-statement)

### Guard pattern matching
Code:

    def guard_pattern_matching(color):
        """Guard pattern matching."""

        match color:
            case r, g, b:
                print(f'Where is the alpha channel?')
                print(f'r={r}, g={g}, b={b}', end='\n\n')
            case r, g, b, a if r == 0 and g == 0 and b == 0:
                print(f'Black: {r}, {g}, {b}, {a}', end='\n\n')
            case r, g, b, a if r == 255 and g == 255 and b == 255:
                print(f'White: {r}, {g}, {b}, {a}', end='\n\n')
            case r, g, b, a if a == 0:
                print(f'Alpha channel is transparent: {a}')
                print(f'r={r}, g={g}, b={b}, a={a}', end='\n\n')
            case r, g, b, a if a == 1:
                print(f'Alpha channel is opaque: {a}')
                print(f'r={r}, g={g}, b={b}, a={a}', end='\n\n')
            case r, g, b, a if a == 0.5:
                print(f'Alpha channel is 50% transparent: {a}')
                print(f'r={r}, g={g}, b={b}, a={a}', end='\n\n')
            case _:
                print(f'Color does not match pattern.', end='\n\n')

    print(' Guard pattern matching '.center(80, '-').title())
    guard_pattern_matching((205, 255, 255))
    guard_pattern_matching((0, 0, 0, 1))
    guard_pattern_matching((255, 255, 255, 1))
    guard_pattern_matching([205, 255, 255, 0])
    guard_pattern_matching([205, 255, 255, 1])
    guard_pattern_matching([205, 255, 255, 0.5])
    guard_pattern_matching([205, 255, 255, 0.5, 0.5])
    
Result:

    ---------------------------- Guard Pattern Matching ----------------------------
    Where is the alpha channel?
    r=205, g=255, b=255
    
    Black: 0, 0, 0, 1
    
    White: 255, 255, 255, 1
    
    Alpha channel is transparent: 0
    r=205, g=255, b=255, a=0
    
    Alpha channel is opaque: 1
    r=205, g=255, b=255, a=1
    
    Alpha channel is 50% transparent: 0.5
    r=205, g=255, b=255, a=0.5
    
    Color does not match pattern.

[🔝](#pattern-matching-statement)

### Irrefutable case blocks
Code:

    def irrefutable_case_blocks_with_wildcard(action):
        """Irrefutable case blocks with wildcard."""
        match action.split():
            case 'move', 'up' | 'down' as direction:  # | is the union operator
                print(f'Moving {direction}', end='\n\n')
            case 'move', 'left' | 'right' as direction:
                print(f'Moving {direction}', end='\n\n')
            # case 'move', *_ as direction:  # * is the splat operator
            #     print(f'Moving {direction}', end='\n\n')
            case 'move', *_, 'fast' as direction:
                print(f'Moving {direction} fast', end='\n\n')
            case 'move', *_, 'slow' as direction:
                print(f'Moving {direction} slow', end='\n\n')
            case 'move', *_, 'fast', 'fast' as direction:
                print(f'Moving {direction} fast fast', end='\n\n')
            case 'move', *_, 'slow', 'slow' as direction:
                print(f'Moving {direction} slow slow', end='\n\n')

    print(' Irrefutable case blocks '.center(80, '-').title())
    irrefutable_case_blocks_with_wildcard('move up')
    irrefutable_case_blocks_with_wildcard('move down')
    irrefutable_case_blocks_with_wildcard('move left')
    irrefutable_case_blocks_with_wildcard('move right')
    irrefutable_case_blocks_with_wildcard('move fast')
    irrefutable_case_blocks_with_wildcard('move slow')
    irrefutable_case_blocks_with_wildcard('move fast fast')
    irrefutable_case_blocks_with_wildcard('move slow slow')
    irrefutable_case_blocks_with_wildcard('move fast fast fast')
    irrefutable_case_blocks_with_wildcard('move slow slow slow')

Result:

    --------------------------- Irrefutable Case Blocks ----------------------------
    Moving up
    
    Moving down
    
    Moving left
    
    Moving right
    
    Moving fast fast
    
    Moving slow slow
    
    Moving fast fast
    
    Moving slow slow
    
    Moving fast fast
    
    Moving slow slow

[🔝](#pattern-matching-statement)

### Matching patterns in classes
Code:

    class ServiceLevel:
        def __init__(self, subscription, msg_type):
            self.subscription = subscription
            self.msg_type = msg_type
    
        def get_service_level(self):
            match self:
                case ServiceLevel(subscription=_, msg_type='info'):
                    print(
                        'Level = 0',
                        f'Subscription = {self.subscription}',
                        f'Msg type = {self.msg_type}',
                        sep='\n',
                        end='\n\n'
                    )
                case ServiceLevel(subscription='free', msg_type='error'):
                    print(
                        'Level = 1',
                        f'Subscription = {self.subscription}',
                        f'Msg type = {self.msg_type}',
                        sep='\n',
                        end='\n\n'
                    )
                case ServiceLevel(subscription='premium', msg_type='error'):
                    print(
                        'Level = 2',
                        f'Subscription = {self.subscription}',
                        f'Msg type = {self.msg_type}',
                        sep='\n',
                        end='\n\n'
                    )
                case _:
                    print('Provide valid parameters')

    print(' Matching patterns in classes '.center(80, '-').title())
    ServiceLevel('free', 'info').get_service_level()
    ServiceLevel('free', 'error').get_service_level()
    ServiceLevel('premium', 'error').get_service_level()
    ServiceLevel('premium', 'info').get_service_level()

Result:

    ------------------------- Matching Patterns In Classes -------------------------
    Level = 0
    Subscription = free
    Msg type = info
    
    Level = 1
    Subscription = free
    Msg type = error
    
    Level = 2
    Subscription = premium
    Msg type = error
    
    Level = 0
    Subscription = premium
    Msg type = info

[🔝](#pattern-matching-statement)