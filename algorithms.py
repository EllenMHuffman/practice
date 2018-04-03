# Given a list of ~1,000,000 numbers in random order, find the largest 10
# elements of the list.


def find_largest_ten(large_list):
    """Given list of integers, return a list of the 10 largest elements."""
    merge_sort(large_list)
    largest_ten = large_list[-10:]

    return largest_ten


def merge_sort(lst):
    """Recursively split list and merge in sorted order. In place."""

    if len(lst) < 2:
        return

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

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
