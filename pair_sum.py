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
