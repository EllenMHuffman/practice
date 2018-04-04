# Given list of integers, determine if there is a pair that sums up to k.


def has_sum(nums, k):
    """Determines whether two numbers sum to given number k.

    >>> has_sum([1,2,3,4,5,2], 4)
    True
    >>> has_sum([2,3,4,5], 4)
    False
    >>> has_sum([1,2,3], 10)
    False

    """

    for i, num in enumerate(nums[:-1]):
        for alt in nums[i + 1:]:
            if num + alt == k:
                return True

    return False


def find_triple_sums(nums, k):
    """Returns all sets of 3 elements that sum to k.

    >>> find_triple_sums([1,2,3], 6)
    [[1, 2, 3]]
    >>> find_triple_sums([1,2,3,6,7], 10)
    [[1, 2, 7], [1, 3, 6]]
    """

    triple_sets = []

    for i, num in enumerate(nums[:-2]):
        for j, alt in enumerate(nums[i + 1:-1]):
            for third in nums[j + 1:]:
                if num + alt + third == k:
                    triple_sets.append([num, alt, third])

    return triple_sets
