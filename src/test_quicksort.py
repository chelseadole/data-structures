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


def test_quicksort_on_len_1():
    """Test quicksort on a list length one."""
    assert quick_sort([1]) == [1]


def test_quicksort_on_len_2():
    """Test quicksort on a list length one."""
    assert quick_sort([3, 2]) == [2, 3]


def test_quicksort_on_medlength_list():
    """Test quicksort on a list length one."""
    assert quick_sort([33, 25, 1, 90, 8302, 733]) == [1, 25, 33, 90, 733, 8302]


def test_quicksort_on_backwards_list():
    """Test quicksort on a list in worstcase scenario."""
    assert quick_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_quicksort_on_pre_sorted_list():
    """Test quicksort on a list in bestcase scenario."""
    assert quick_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_quicksort_on_list_with_negatives():
    """Test quicksort on a list with neg numbers.."""
    assert quick_sort([-1, -2, -3, 4, 5, 6, 7, 8, -9, 10]) == [-9, -3, -2, -1, 4, 5, 6, 7, 8, 10]
