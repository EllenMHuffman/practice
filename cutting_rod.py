# Given a rod of length n inches and an array of prices, return the maximum
# value that can be obtained by cutting up the rod


def cut_rod(price, n):
    """Determine max value out of cut rod given prices for lengths. Exponential.

    >>> cut_rod([1, 5, 8, 9, 10, 17, 17, 20], 8)
    22
    >>> cut_rod([3, 5, 8, 9, 10, 17, 17, 20], 8)
    24

    """

    max_val = 0

    for i in range(n):
        max_val = max(max_val, price[i] + cut_rod(price, n - i - 1))

    return max_val


def cut_rod_optimal(price, n):
    """Determine max value of cut rod.

    >>> cut_rod_optimal([1, 5, 8, 9, 10, 17, 17, 20], 8)
    22
    >>> cut_rod_optimal([3, 5, 8, 9, 10, 17, 17, 20], 8)
    24

    """

    val = [0] * (n + 1)

    for i in range(n + 1):
        max_val = -1

        for j in range(i):
            max_val = max(max_val, price[j] + val[i - j - 1])
            val[i] = max_val

    return val[n]
