"""Implementation of Bubble Sort in Python."""


def bubblesort(lst):
    """Bubble sorting algorithm."""
    if isinstance(lst, list):
        for i in range(len(lst)):
            for j in range(len(lst) - 1, i, -1):
                if lst[j] < lst[j - 1]:
                    lst[j], lst[j - 1] = lst[j - 1], lst[j]
        return lst
    return "BubbleSort takes only lists."

if __name__ == '__main__':  # pragama: no cover
    import timeit as ti
    import random
    best_case = [1, 2, 3, 4, 5]
    worst_case = [5, 4, 3, 2, 1]
    random = [random.randint(1, 100) for i in range(10)]

    time_1 = ti.timeit("bubblesort(best_case)",
                       setup="from __main__ import best_case, bubblesort")
    time_2 = ti.timeit("bubblesort(worst_case)",
                       setup="from __main__ import worst_case, bubblesort")
    time_3 = ti.timeit("bubblesort(random)",
                       setup="from __main__ import random, bubblesort")
    print("""
Bubblesort sorts an input numerically from smallest to largest number by
stepping through each index, and (if the value of the index above it is lower)
swapping the current index with the current index + 1.

Input:[1, 2, 3, 4, 5]
Sort time: {}

Input:[5, 4, 3, 2, 1]
Sort time: {}

Input:list(range(5, 0, -1))
Sort time: {}
    """.format(time_1, time_2, time_3))
