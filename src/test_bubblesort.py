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


