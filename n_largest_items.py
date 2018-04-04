# Given a list of ~1,000,000 numbers in random order, find the largest 10
# elements of the list.


def find_k_largest(k, numbers):
    """Find the k largest elements in given list. O(nk) runtime."""

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    items = [None] * (largest + 1)

    for num in numbers:
        items[num] = num

    largest_items = []

    for item in reversed(items):
        if item is not None:
            largest_items.append(item)
        if len(largest_items) == k:
            return largest_items
