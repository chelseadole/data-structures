"""Testing module for insertion sort algorithm."""

import pytest
from insertion_sort import insertion_sort
from random import randint



def test_ins_sort_on_empty_lst():
    """Sort on empty list as input."""
    assert insertion_sort([]) == []


def test_ins_sort_on_lst_len_1():
    """Test on a list with one thing in it."""
    assert insertion_sort([1]) == [1]


def test_ins_sort_on_lst_len_2():
    """Test ins sort on a list with two unordered nums."""
    assert insertion_sort([53, 2]) == [2, 53]


def test_ins_sort_on_dictionary():
    """Test ins sort with input of dictionary."""
    with pytest.raises(TypeError):
        assert insertion_sort({'1': 1, '2': 2})


def test_ins_sort_on_string():
    """Test insertion doesnt work with string input."""
    with pytest.raises(TypeError):
        assert insertion_sort("this wont work")


def test_list_with_non_num_inside():
    """Test on a list with a string as one of the items."""
    with pytest.raises(TypeError):
        assert insertion_sort([1, 2, 3, 4, 'five', 6, 7])


def test_list_with_negatives():
    """Test on list with neg numbers."""
    assert insertion_sort([-32, 23, 1, 0, 900, -14]) == [-32, -14, 0, 1, 23, 900]


def test_list_on_randomized_lists():
    """Test using randomly generated lists."""
    for i in range(60):
        lst = [randint(0, 1000) for i in range(30)]
        sorted_lst = sorted(lst)
        assert insertion_sort(lst) == sorted_lst


def test_list_on_randomized_long_lists():
    """Test using randomly generated lists."""
    for i in range(15):
        long_lst = [randint(0, 1000) for i in range(100)]
        sorted_long_lst = sorted(long_lst)
        assert insertion_sort(long_lst) == sorted_long_lst
