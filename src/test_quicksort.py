"""Testing module for quick_sort algorithm."""

import pytest
from quicksort import quick_sort


def test_quicksort_on_empty_list():
    """Empty list test."""
    assert quick_sort([]) == []


def test_quicksort_on_set():
    """Run quicksort on set."""
    with pytest.raises(TypeError):
        assert quick_sort((1, 2)) == [1, 2]


def test_quicksort_on_dict():
    """Run quicksort on set."""
    with pytest.raises(TypeError):
        assert quick_sort({}) == [1, 2]
