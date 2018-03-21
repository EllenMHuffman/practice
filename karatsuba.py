# x * y = 10^n * ac + 10^(n/2) * (ad + bc) + bd


def multiply(num1, num2):
    """Recursively multiply two numbers using Karatsuba method."""

    num1 = str(num1)
    num2 = str(num2)

    if len(num1) == 1 and len(num2) == 1:
        return int(num1) * int(num2)

    n = len(num1)
    split = int(n / 2)
    # import pdb; pdb.set_trace()
    a = num1[:split]
    b = num1[split:]
    c = num2[:split]
    d = num2[split:]

    term1 = 10 ** n * (multiply(a, c))
    term2 = 10 ** (n / 2) * (multiply(a, d) + multiply(b, c))
    term3 = multiply(b, d)

    result = term1 + term2 + term3

    return result
