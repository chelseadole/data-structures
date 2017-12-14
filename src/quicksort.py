"""Quick sort algorithm."""


def quick_sort(a_list):
    """Quick sort a list."""
    if not isinstance(a_list, list):
        raise TypeError("Lists are the only valid input.")
    if len(a_list) < 2:
        return a_list
    ref = [a_list.pop(0)]
    smaller = []
    bigger = []

    for x in a_list:
        if x < ref[0]:
            smaller.append(x)

        else:
            bigger.append(x)

    return quick_sort(smaller) + ref + quick_sort(bigger)

if __name__ == '__main__':  # pragama: no cover
    import timeit as ti
    import random
    best_case = [1, 2, 3, 4, 5]
    worst_case = [5, 4, 3, 2, 1]
    random = [random.randint(1, 100) for i in range(10)]

    time_1 = ti.timeit("quick_sort(best_case)",
                       setup="from __main__ import best_case, quick_sort")
    time_2 = ti.timeit("quick_sort(worst_case)",
                       setup="from __main__ import worst_case, quick_sort")
    time_3 = ti.timeit("quick_sort(random)",
                       setup="from __main__ import random, quick_sort")
    print("""
Quicksort divides the numbers into 'smaller' and 'bigger' than a pivot number, and redivides until it finds the correct order.

Input:[1, 2, 3, 4, 5]
Sort time: {}

Input:[5, 4, 3, 2, 1]
Sort time: {}

Input:list(range(5, 0, -1))
Sort time: {}
    """.format(time_1, time_2, time_3))
