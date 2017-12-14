"""Insertion sort algorithm."""


def insertion_sort(lst):
    """Implementation of insertion sort in python."""
    if isinstance(lst, list):
        for i in range(1, len(lst)):
            curr = lst[i]
            if not isinstance(i, int):
                raise TypeError('Only integers can be in the list.')
            while i > 0 and lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                i -= 1
            i = curr
        return lst
    raise TypeError('Only lists can be used with Insertion Sort.')
