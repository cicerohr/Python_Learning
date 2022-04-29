# -*- coding: utf-8 -*-
r"""pattern_matching.py in: 2022-04-28.

Python version: 3.10.0

Pattern matching.
"""
from tests.loguru_conf import logger


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
            print('diferente de 1, 2 e 3')


def http_error(status_code):
    """HTTP error."""
    match status_code:
        case 200:
            print('OK')
        case 400:
            print('Bad Request')
        case 404:
            print('Not Found')
        case 418:
            print('I\'m a teapot')
        case _:
            print('Unknown error')


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


def main():
    """Main function."""
    print(' Pattern matching with literals '.center(80, '-').title())
    pattern_matching_switch_case(1)
    pattern_matching_switch_case(2)
    pattern_matching_switch_case(3)
    pattern_matching_switch_case(4)
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
    print(' Naming elements in pattern matching '.center(80, '-').title())
    naming_elements_in_pattern_matching((255, 255, 255))
    naming_elements_in_pattern_matching((255, 255, 255, 255))
    naming_elements_in_pattern_matching((255, 255, 255, 255, 255))
    naming_elements_in_pattern_matching((255, 255, 255, 255, 255, 255))
    print(' Guard pattern matching '.center(80, '-').title())
    guard_pattern_matching((205, 255, 255))
    guard_pattern_matching((0, 0, 0, 1))
    guard_pattern_matching((255, 255, 255, 1))
    guard_pattern_matching([205, 255, 255, 0])
    guard_pattern_matching([205, 255, 255, 1])
    guard_pattern_matching([205, 255, 255, 0.5])
    guard_pattern_matching([205, 255, 255, 0.5, 0.5])


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
