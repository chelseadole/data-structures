"""Testing module for BubbleSort algorithm."""

from bubblesort import bubblesort
import pytest


def test_bubblesort_with_empty_lst():
    """Bubble sort returns empty list with input empy lst."""
    empty = []
    assert bubblesort(empty) == []


def test_bubble_sort_doesnt_work_on_string():
    """Bubble sort cannot be given a string as input."""
    wrong_str = "This will raise an exception"
    assert bubblesort(wrong_str) == "BubbleSort takes only lists."


def test_bubble_sort_doesnt_work_on_set():
    """Bubble sort cannot be given set as input."""
    wrong_set = (1, 2, 3, 4)
    assert bubblesort(wrong_set) == "BubbleSort takes only lists."


def test_bubble_sort_doesnt_work_on_dict():
    """Bubble sort cannot be given set as input."""
    wrong_dict = {"1": 1, "2": 2, "3": 3}
    assert bubblesort(wrong_dict) == "BubbleSort takes only lists."


def test_bubble_sort_can_sort_len_2_lst():
    """Bubble sort sorts unordered lst, where len(lst) == 2."""
    two_idx_lst = [44, 1]
    assert bubblesort(two_idx_lst) == [1, 44]


def test_bubble_sort_works_on_longer_lst():
    """Bubble sort sorts unordered_lst, where len(lst) == 16."""
    longer_lst = [33, 26, 900, 22, 34, 1, 0, 2000, 22, 20, 90, 99, 200, 322, 1000]
    assert bubblesort(longer_lst) == [0, 1, 20, 22, 22, 26, 33, 34, 90, 99, 200, 322, 900, 1000, 2000]


def test_bubble_sort_works_on_negatives():
    """Bubble sort on list with negative numbers."""
    neg_lst = [-30, 20, -200, -1, -3, 13]
    assert bubblesort(neg_lst) == [-200, -30, -3, -1, 13, 20]


def test_bubble_sort_on_presorted_lst():
    """Bubble sort does not change input lst that is already sorted."""
    pre_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert bubblesort(pre_sorted) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

