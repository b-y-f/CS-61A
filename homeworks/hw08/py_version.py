isEven = lambda x: x % 2 == 0
isOdd = lambda x: x % 2 != 0


def myfilter(func, lst):
    """
    >>> a = [1,2,3,4]
    >>> myfilter(isEven, a )
    [2, 4]
    >>> myfilter(isOdd, a)
    [1, 3]
    """
    if not lst:
        return []
    elif func(lst[0]):
        return [lst[0]] + myfilter(func, lst[1:])
    else:
        return myfilter(func, lst[1:])


def interleave(s1, s2):
    """
    >>> a = [1,3,5]
    >>> b = [2,4,6]
    >>> c = [2]
    >>> interleave(a,b)
    [1, 2, 3, 4, 5, 6]
    >>> interleave(a,b)
    [1, 2, 3, 5]
    """
    if not s1 or not s2:
        return []
    else:
        return interleave()