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

if __name__ == '__main__':  # pragama: no cover
    import timeit as ti
    import random
    best_case = [1, 2, 3, 4, 5]
    worst_case = [5, 4, 3, 2, 1]
    random = [random.randint(1, 100) for i in range(10)]

    time_1 = ti.timeit("insertion_sort(best_case)",
                       setup="from __main__ import best_case, insertion_sort")
    time_2 = ti.timeit("insertion_sort(worst_case)",
                       setup="from __main__ import worst_case, insertion_sort")
    time_3 = ti.timeit("insertion_sort(random)",
                       setup="from __main__ import random, insertion_sort")
    print("""
Insertion sort compares the vals of an index versus the index - 1, and
(if index is smaller) switches. Them it continues switching until index is
bigger than index - 1.

Input:[1, 2, 3, 4, 5]
Sort time: {}

Input:[5, 4, 3, 2, 1]
Sort time: {}

Input:list(range(5, 0, -1))
Sort time: {}
    """.format(time_1, time_2, time_3))

