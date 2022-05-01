from unittest import TestCase

from src.sorted_list_search import (
    binary_search,
    interpolation_search,
    linear_search,
)


class TestAlgorithms(TestCase):
    def test_linear_search(self):
        assert linear_search([1, 2, 3, 4, 5], 5) == 4

    def test_linear_search_not_found(self):
        assert linear_search([1, 2, 3, 4, 5], 6) == -1

    def test_linear_search_empty_list(self):
        assert linear_search([], 1) == -1

    def test_linear_search_one_element_list(self):
        assert linear_search([1], 1) == 0

    def test_binary_search(self):
        assert binary_search([1, 2, 3, 4, 5], 5) == 4

    def test_binary_search_not_found(self):
        assert binary_search([1, 2, 3, 4, 5], 6) == -1

    def test_binary_search_empty_list(self):
        assert binary_search([], 1) == -1

    def test_binary_search_one_element_list(self):
        assert binary_search([1], 1) == 0

    def test_interpolation_search(self):
        assert interpolation_search([1, 2, 3, 4, 5], 5) == 4

    def test_interpolation_search_not_found(self):
        assert interpolation_search([1, 2, 3, 4, 5], 6) == -1

    def test_interpolation_search_empty_list(self):
        assert interpolation_search([], 1) == -1

    def test_interpolation_search_one_element_list(self):
        assert interpolation_search([1], 1) == 0
