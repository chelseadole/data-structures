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
