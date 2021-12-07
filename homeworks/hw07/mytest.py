def ordered(s):
    """
    >>> ordered([1,2,3])
    True
    >>> ordered([1,2,2,3])
    True
    >>> ordered([2,1,3])
    False
    >>> ordered([1,2,3,4,3])
    False
    >>> ordered([1,2,3,3,2])
    False
    """
    if not s[1:]:
        return True
    rest = s[1:]
    if s[0] > rest[0]:
        return False
    return ordered(rest)


isOdd = lambda x: x % 2 != 0
squre = lambda x: x ** 2


def pow(base, exp):
    """
    >>> pow(1,100000)
    1
    >>> pow(2,3)
    8
    >>> pow(3,3)
    27
    >>> pow(2,5)
    32
    """
    if exp == 0:
        return 1

    if isOdd(exp):
        return pow(base, exp - 1) * base
    else:
        return squre(pow(base, exp / 2))
