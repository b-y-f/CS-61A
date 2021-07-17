# Lists
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i*j for i,j in enumerate(s) if i%2==0]


def closest_number(nums, target):
    """
    >>> closest_number([1, 4, 5, 6, 7], 2)
    1
    >>> closest_number([3, 1, 5, 6, 13], 4) #  choose the earlier number since there's a tie
    3
    >>> closest_number([34, 102, 8, 5, 23], 25)
    23
    """
    return min(nums,key=lambda x:abs(x-target))


# def max_product(s):
#     """Return the maximum product that can be formed using non-consecutive
#     elements of s.

#     >>> max_product([10,3,1,9,2]) # 10 * 9
#     90
#     >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
#     125
#     >>> max_product([])
#     1
#     """
#     if len(s)==1:
#         return s[0]
#     elif len(s) == 0:
#         return 0
#     else:
#         return max_product


# Dict
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    "*** YOUR CODE HERE ***"
    for ____________________:
        "*** YOUR CODE HERE ***"
        key = _________________
        "*** YOUR CODE HERE ***"
        if ______________________________________:
            "*** YOUR CODE HERE ***"
             ____________________________________________
        else:
            "*** YOUR CODE HERE ***"
            grouped[key] = ___________________________________
    "*** YOUR CODE HERE ***"
    return _________________________________




