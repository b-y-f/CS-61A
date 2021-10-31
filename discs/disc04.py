# new
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"


def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [index*s[index] for index in range(len(s)) if index % 2 == 0]


def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([1,2,3,4,5,6]) # 2*4*6
    48
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    else:
        right, prod = max_product(s[1:]), s[0] * max_product(s[2:])
        return max(prod, right)





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
    for i in s:
        "*** YOUR CODE HERE ***"
        key = fn(i)
        "*** YOUR CODE HERE ***"
        if key in grouped:
            "*** YOUR CODE HERE ***"
            grouped[key].append(i)
        else:
            "*** YOUR CODE HERE ***"
            grouped[key] = [i]
    "*** YOUR CODE HERE ***"
    return grouped



# Exam Prep

def subset_sum(target, lst):
    """Returns True if it is possible to add some of the integers in lst
    to get target.

    >>> subset_sum(10, [-1, 5, 4, 6])
    True
    >>> subset_sum(4, [5, -2, 12])
    False
    >>> subset_sum(-3, [5, -2, 2, -2, 1])
    True
    >>> subset_sum(0, [-1, -3, 15])     # Sum up none of the numbers to get 0
    True
    """
    # TODO dont know hint: target-->0
    if target == 0:
        return True
    elif len(lst)<1:
        return False
    else:
        a = subset_sum(target-lst[0],lst[1:]) 
        b = ... #  hint: keep same situation
        return a or b


def intersection(lst_of_lsts):
    """Returns a list of distinct elements that appear in every list in
    lst_of_lsts.

    >>> lsts1 = [[1, 2, 3], [1, 3, 5]]
    >>> intersection(lsts1)
    [1, 3]
    >>> lsts2 = [[1, 4, 2, 6], [7, 2, 4], [4, 4]]
    >>> intersection(lsts2)
    [4]
    >>> lsts3 = [[1, 2, 3], [4, 5], [7, 8, 9, 10]]
    >>> intersection(lsts3)         # No number appears in all lists
    []
    >>> lsts4 = [[3, 3], [1, 2, 3, 3], [3, 4, 3, 5]]
    >>> intersection(lsts4)         # Return list of distinct elements
    [3]
    """
    elements = []
    for i in lst_of_lsts[0]:
        condition = i not in elements
        for j in lst_of_lsts[1:]:
            if i not in j:
                condition = False
        if condition:
            elements = elements + [i]
    return elements



def wordify(s):
    """ Takes a string s and divides it into a list of words. Assume that the last element of the string is a whitespace.
    Duplicate words allowed.
    >>> wordify ('sum total of human knowledge ')
    ['sum', 'total', 'of', 'human', 'knowledge']
    >>> wordify ('one should never use exclamation points in writing! ')
    ['one', 'should', 'never', 'use', 'exclamation', 'points', 'in', 'writing!']
    """
    # start, end, lst = '', ' ', []
    # for letter in s:
    #     if letter != ' ':
    #         end = end + letter
    #     elif start == end :
    #         start, end = '', ''
    #     else :
    #         lst +=  [end[1:]]
    #         start, end = letter, letter
    # return lst

    # another solution
    start, end, lst = 0, 0, []
    for letter in s:
            if letter != ' ':
                end = end + 1
            elif start == end :
                start, end = 0, 0
            else :
                lst +=  [s[start:end]]
                start, end = end+1, end+1
    return lst
