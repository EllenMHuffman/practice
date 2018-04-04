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


def has_sum_optimized(nums, k):
    """Determines whether two numbers sum to given number k.

    >>> has_sum_optimized([1,2,3,4,5,2], 4)
    True
    >>> has_sum_optimized([2,3,4,5], 4)
    False
    >>> has_sum_optimized([1,2,3], 10)
    False

    """

    nums.sort()
    l = 0
    r = len(nums) - 1

    while l < r:
        if nums[l] + nums[r] == k:
            return True
        elif nums[l] + nums[r] < k:
            l += 1
        else:
            r -= 1

    return False


def find_triple_sums(nums, k):
    """Returns all sets of 3 elements that sum to k. O(n^3) runtime.

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


def find_triplets(nums, k):
    """Returns all triplets that sum to k. O(n^2) runtime.

    >>> find_triplets([1,2,3], 6)
    [[1, 2, 3]]
    >>> find_triplets([1,2,3,6,7], 10)
    [[1, 2, 7], [1, 3, 6]]

    """

    triplets = []

    nums.sort()

    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1

        while l < r:
            if nums[i] + nums[l] + nums[r] == k:
                triplets.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
            elif nums[i] + nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1

    return triplets
