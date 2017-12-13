"""Insertion sort algorithm."""


def insertion_sort(lst):
    """Implementation of insertion sort in python."""
    if isinstance(lst, list):
        if 
        for i in lst[1:]:
            while lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                i -= 1
