import re


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
    >>> c = [2,4]
    >>> interleave(a,b)
    [1, 2, 3, 4, 5, 6]
    >>> interleave(a,c)
    [1, 2, 3, 4, 5]
    """
    if len(s1) == 0 or len(s2) == 0:
        return s1 + s2
    else:
        return [s1[0]] + [s2[0]] + interleave(s1[1:],s2[1:])



def no_repeats(lst):
    """
    >>> a = [1,2,2,3,3,4]
    >>> no_repeats(a)
    [1, 2, 3, 4]
    """
    if len(lst) == 0:
        return []
    return [lst[0]] + no_repeats(list(filter(lambda x:x!=lst[0], lst[1:])))
 