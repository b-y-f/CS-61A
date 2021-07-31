# from https://cs61a.org/study-guide/recursion/

def sum(n):
    """Computes the sum of all integers between 1 and n, inclusive.
    Assume n is positive.

    >>> sum(1)
    1
    >>> sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    else:
        return sum(n-1)+n


def sine(x):
    "*** YOUR CODE HERE ***"

    if x<0.01:
        return x
    else:
        return  3*sine(x/3) - 4*(sine(x/3)**3)

# print (sine(123))

def countdown_up(n):
    """Starts at n and simultaneously prints out the countdown from n to 0
    and the countup from n to 2*n, inclusive.

    >>> countdown_up(0)
    0

    >>> countdown_up(5)
    5
    4
    6
    3
    7
    2
    8
    1
    9
    0
    10
    """
    "*** YOUR CODE HERE ***"


    


def mario_number(level):
    """Return the number of ways that Mario can perform a sequence of steps
    or jumps to reach the end of the level without ever landing in a Piranha
    plant. Assume that every level begins and ends with a space.

    >>> mario_number(' P P ')   # jump, jump
    1
    >>> mario_number(' P P  ')   # jump, jump, step
    1
    >>> mario_number('  P P ')  # step, jump, jump
    1
    >>> mario_number('   P P ') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number(' P PP ')  # Mario cannot jump two plants
    0
    >>> mario_number('    ')    # step, jump ; jump, step ; step, step, step
    3
    >>> mario_number('    P    ')
    9
    >>> mario_number('   P    P P   P  P P    P     P ')
    180
    """
    "*** YOUR CODE HERE ***"
    