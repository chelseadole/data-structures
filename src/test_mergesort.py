"""Mergesort sorting algorithm."""

from mergesort import merge_sort
import pytest


def test_mergesort_on_empty_lst():
    """Mergesort on empty list."""
    lst = []
    assert merge_sort(lst) == []


def test_mergesort_on_a_set():
    """Test mergesort on set."""
    not_a_list = set()
    with pytest.raises(TypeError):
        assert merge_sort(not_a_list)


def test_mergesort_on_a_dict():
    """Test mergesort on set."""
    not_a_list = {"1": 1, "2": 2}
    with pytest.raises(TypeError):
        assert merge_sort(not_a_list)


def test_mergesort_on_medlength_lst():
    """Mergesort on med length list."""
    lst = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    assert merge_sort(lst) == [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]


def test_sort_on_lst_len_1():
    """Test mergesort on a list that is one item long."""
    lst = [1]
    assert merge_sort(lst) == [1]


def test_on_pre_sorted_list():
    """Test mergesort on a list that is already sorted."""
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge_sort(lst) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_on_backwards_list():
    """Test mergesort on a list that is already sorted."""
    lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert merge_sort(lst) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
