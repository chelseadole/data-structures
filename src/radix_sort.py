"""Radix Sorting Algorithm."""


def radix_sort(lst):
    """Implementation of Radix Sort in python."""
    if not isinstance(lst, list):
        raise TypeError('Input must be a list of integers.')
    if len(lst) == 0:
        return lst
    str_lst = [str(i) for i in lst]
    largest_int_len = len(str(max(lst)))

    for rep_num in range(largest_int_len):
        buckets = [[] for i in range(10)]
        for str_int in str_lst:
            if len(str_int) < rep_num + 1:
                buckets[0].append(int(str_int))
            else:
                target = buckets[int(str_int[0])]
                target.append(str_int)
        flat_list = _append(buckets)
        str_lst = flat_list
    return [int(i) for i in flat_list]


def _append(buckets):
    """Helper function to flatten buckets into a single list."""
    flat_list = []
    for bucket in buckets:
        for num in bucket:
            flat_list.append(str(num))
    return flat_list