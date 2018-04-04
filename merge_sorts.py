

def merge_sort_inplace(lst):
    """Recursively split list and merge in sorted order. In place."""

    if len(lst) < 2:
        return

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    merge_sort_inplace(left_half)
    merge_sort_inplace(right_half)

    i = 0  # tracks index of left half
    j = 0  # tracks index of right half
    k = 0  # tracks index of parent list

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            lst[k] = left_half[i]
            i += 1
        else:
            lst[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        lst[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        lst[k] = right_half[j]
        j += 1
        k += 1
################################################################################


def merge(a, b):
    """Merge two sorted lists together."""

    c = []

    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)

    if len(a) == 0:
        c += b

    if len(b) == 0:
        c += a

    return c


def merge_sort_newlist(lst):
    """Recursively split list and merge in sorted order. Creates new list."""

    if len(lst) < 2:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    a = merge_sort_newlist(left_half)
    b = merge_sort_newlist(right_half)

    c = merge(a, b)

    return c
