"""Testing module for Radix Sort algorithm."""

from radix_sort import radix_sort
import pytest


def test_radix_sort_with_empty_lst():
    """Radixsort returns empty list with input empy lst."""
    empty = []
    assert radix_sort(empty) == []


def test_radix_sort_doesnt_work_on_string():
    """Radix sort cannot be given a string as input."""
    with pytest.raises(TypeError):
        wrong_str = "This will raise an exception"
        assert radix_sort(wrong_str)


def test_radix_sort_doesnt_work_on_set():
    """Radix sort cannot be given a set as input."""
    with pytest.raises(TypeError):
        wrong_set = (1, 2, 3)
        assert radix_sort(wrong_set)


def test_radix_sort_doesnt_work_on_dict():
    """Radix sort cannot be given set as input."""
    with pytest.raises(TypeError):
        wrong_dict = {"1": 1, "2": 2, "3": 3}
        assert radix_sort(wrong_dict)


def test_radix_sort_can_sort_len_2_lst():
    """Radix sort sorts unordered lst, where len(lst) == 2."""
    two_idx_lst = [44, 1]
    assert radix_sort(two_idx_lst) == [1, 44]


def test_radix_sort_works_on_longer_lst():
    """Radix sort sorts unordered_lst, where len(lst) == 16."""
    longer_lst = [33, 26, 900, 22, 34, 1, 0, 2000, 22, 20, 90, 99, 200, 322, 1000]
    assert radix_sort(longer_lst) == [0, 1, 20, 22, 22, 26, 33, 34, 90, 99, 200, 322, 900, 1000, 2000]


def test_radix_sort_works_on_negatives():
    """Radix sort on list with negative numbers."""
    neg_lst = [-30, 20, -200, -1, -3, 13]
    assert radix_sort(neg_lst) == [-200, -30, -3, -1, 13, 20]


def test_radix_sort_on_presorted_lst():
    """Radix sort does not change input lst that is already sorted."""
    pre_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert radix_sort(pre_sorted) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
