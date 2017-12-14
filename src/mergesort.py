"""Merge sort algorithm."""


def merge_sort(a_list):
    """Use MS to sort the provided list and return it."""
    if not isinstance(a_list, list):
        raise TypeError("Only list is a valid input type!")

    if len(a_list) < 2:
        return a_list

    parts = [[i] for i in a_list]

    while len(parts) > 1:
        if len(parts[0]) == len(parts[1]) or len(parts) == 2:
            parts.insert(0, _merge(parts.pop(0), parts.pop(0)))
        else:
            parts.insert(0, _merge(parts.pop(0), _merge(parts.pop(0), parts.pop(0))))
    return parts[0]


def _merge(part_a, part_b):
    """."""
    temp = []
    while part_a and part_b:
        if part_a[0] <= part_b[0]:
            temp.append(part_a.pop(0))
        else:
            temp.append(part_b.pop(0))

    while part_a:
        temp.append(part_a.pop(0))

    while part_b:
        temp.append(part_b.pop(0))

    return temp

if __name__ == '__main__':  # pragama: no cover
    import timeit as ti
    import random
    best_case = [1, 2, 3, 4, 5]
    worst_case = [5, 4, 3, 2, 1]
    random = [random.randint(1, 100) for i in range(10)]

    time_1 = ti.timeit("merge_sort(best_case)",
                       setup="from __main__ import best_case, merge_sort")
    time_2 = ti.timeit("merge_sort(worst_case)",
                       setup="from __main__ import worst_case, merge_sort")
    time_3 = ti.timeit("merge_sort(random)",
                       setup="from __main__ import random, merge_sort")
    print("""
Mergesort sorts shit by merging it.

Input:[1, 2, 3, 4, 5]
Sort time: {}

Input:[5, 4, 3, 2, 1]
Sort time: {}

Input:list(range(5, 0, -1))
Sort time: {}
    """.format(time_1, time_2, time_3))