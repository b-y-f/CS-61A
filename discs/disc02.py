# Higher Order Functions

def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    "*** YOUR CODE HERE ***"

    for i in range(1,n+1):
        if cond(i) :
            print(i)

def make_keeper(n):
    """Returns a function which takes one parameter cond and 
    prints out all integers 1..i..n where calling cond(i) returns True.
        >>> def is_even(x):
        ...     # Even numbers have remainder 0 when divided by 2.
        ...     return x % 2 == 0
        >>> make_keeper(5)(is_even)
        2
        4
    """
    "*** YOUR CODE HERE ***"
    def f(func):
        for i in range(1,n+1):
            if func(i):
                print(i)
    return f


# Currying
def curry2(h):
    return lambda x : lambda y : h(x,y)

make_adder = curry2(lambda x, y: x + y)
add_three = make_adder(3)
add_four = make_adder(4)
five = add_three(2)

print(five)

def make_keeper_redux(n):
    """Returns a function. This function takes one parameter <cond> and prints out
       all integers 1..i..n where calling cond(i) returns True. The returned
       function returns another function with the exact same behavior.

        >>> def multiple_of_4(x):
        ...     return x % 4 == 0
        >>> def ends_with_1(x):
        ...     return x % 10 == 1
        >>> k = make_keeper_redux(11)(multiple_of_4)
        4
        8
        >>> k = k(ends_with_1)
        1
        11

    """
    # Paste your code for make_keeper here!
    def do_keep(func):
        for i in range(1,n+1):
            if func(i):
                print(i)
        return make_keeper_redux(n)
    return do_keep


def print_delayed(x):
    """Return a new function. This new function, when called, will print out x and return another function with the same behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4

    """    
    # >>> f("hi") # a function is returned
    # 5
    # <function delay_print>
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print


def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)

    """    
    # >>> g("first")("second")("third")
    # first
    # done
    # done
    # <function inner_print>
    def inner_print(x):
        if n<1:
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print


# Exam prep

def match_k(k):
    """ Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def num(n):
        # ____________________________
        while n//(10**k)>0:
            if n %10 != n//(10**k)%10:
                return False
            n = n//10
        return True
    return num


def three_memory(n):
    """
    >>> f = three_memory('first')
    >>> f = f('first')
    Not found
    >>> f = f('second')
    Not found
    >>> f = f('third')
    Not found
    >>> f = f('second') # 'second' was not input three calls ago
    Not found
    >>> f = f('second') # 'second' was input three calls ago
    Found
    >>> f = f('third') # 'third' was input three calls ago
    Found
    >>> f = f('third') # 'third' was not input three calls ago
    Not found
    """
    def f(x, y, z):
        def g(i):
            if x==i:
                print("Found")
            else:
                print("Not found")
            return f(y,z,i)
        return g
    return f(None, None, n)



def chain_function():
    """
    >>> tester = chain_function()
    >>> x = tester(1)(2)(4)(5) # Expected 3 but got 4, so print 3. 1st chain break, so print 1 too.
    3 1
    >>> x = x(2) # 6 should've followed 5 from above, so print 6. 2nd chain break, so print 2
    6 2
    >>> x = x(8) # The chain restarted at 2 from the previous line, but we got 8. 3rd chain break.
    3 3
    >>> x = x(3)(4)(5) # Chain restarted at 8 in the previous line, but we got 3 instead. 4th break
    9 4
    >>> x = x(9) # Similar logic to the above line
    6 5
    >>> x = x(10) # Nothing is printed because 10 follows 9.
    >>> y = tester(4)(5)(8) # New chain, starting at 4, break at 6, first chain break
    6 1
    >>> y = y(2)(3)(10) # Chain expected 9 next, and 4 after 10. Break 2 and 3.
    9 2
    4 3
    """
    def g(x, y): # x:counter y:saved
        def h(n):
            if x==0 or x==n:
                return g(n + 1,y)
            else:
                return print(x,y+1) or g(n+1,y+1)
        return h
    return g(0,0)