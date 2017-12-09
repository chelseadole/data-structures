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

def 