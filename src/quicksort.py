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
