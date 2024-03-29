# OLD Recursion
def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n==1:
        return m
    else :
        return multiply(m,n-1)+m
    

def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    if n1 == 0: 
        return n2
    elif n2 ==0:
        return n1
    elif n1 % 10 > n2 % 10:
        return merge(n1,n2//10)*10 + n2 % 10
    else:
        return merge(n1//10, n2)*10 + n1 % 10


        


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n==1:
        return 1
    elif n%2==0:
        return 1+hailstone(n//2)
    else:
        return hailstone(n*3+1)+1



def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def h(i):
        if i==n:
            return True
        elif n%i==0 :
            return False
        else:
            return h(i+1)

    return h(2)


# Tree Recursion

def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    >>> count_stair_ways(6)
    13
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    elif n==2:
        return 2
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)

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
    if n==0:
        return 1
    elif n<0:
        return 0
    else: #loop??
        sum = 0
        for i in range(1,k+1):
            sum += count_k(n - i, k)
        return sum



# # Exam prep
def is_palindrome(s):
    """
    >>> is_palindrome("tenet")
    True
    >>> is_palindrome("tenets")
    False
    >>> is_palindrome("raincar")
    False
    >>> is_palindrome("")
    True
    >>> is_palindrome("a")
    True
    >>> is_palindrome("ab")
    False
    """
    if len(s)==0:
        return True
    return is_palindrome(s[1:-1]) if s[0]==s[-1] else False


def greatest_pal(s):
    """
    >>> greatest_pal("tenet")
    'tenet'
    >>> greatest_pal("tenets")
    'tenet'
    >>> greatest_pal("stennet")
    'tennet'
    >>> greatest_pal("25 racecars")
    'racecar'
    >>> greatest_pal("abc")
    'a'
    >>> greatest_pal("")
    ''
    """
    
    if is_palindrome(s):
        return s
    left, right = s[:-1],s[1:]
    if is_palindrome(left) or len(left)==2 :
        return greatest_pal(left)
    return greatest_pal(right)

# def greatest_pal(s):
#     """
#     >>> greatest_pal("tenet")
#     'tenet'
#     >>> greatest_pal("tenets")
#     'tenet'
#     >>> greatest_pal("stennet")
#     'tennet'
#     >>> greatest_pal("25 racecars")
#     'racecar'
#     >>> greatest_pal("abc")
#     'a'
#     >>> greatest_pal("")
#     ''
#     """
#     def helper(a, b, c):
#         if __________________________ > ____________________________:
#             return _______________________________________________
#         elif ________________________ > ____________________________:
#             return _______________________________________________
#         elif ________________ and _______________________________
#             ______________________________________________________
#         return ____________________________________________________
#     return helper(1, 0, "")

# def greatest_pal(s):
#     """
#     >>> greatest_pal("tenet")
#     'tenet'
#     >>> greatest_pal("tenets")
#     'tenet'
#     >>> greatest_pal("stennet")
#     'tennet'
#     >>> greatest_pal("25 racecars")
#     'racecar'
#     >>> greatest_pal("abc")
#     'a'
#     >>> greatest_pal("")
#     ''
#     """
#     def helper(a, b):
#         if ______________________________________________________:
#             return ______________________________________________________
#         elif ______________________________________________________:
#             return ______________________________________________________
#         return ______________________________________________________
#     return _________________________________________________________________

# def greatest_pal_two(s):
#     """
#     >>> greatest_pal_two("tenet")
#     'tenet'
#     >>> greatest_pal_two("tenets")
#     'tenet'
#     >>> greatest_pal_two("stennet")
#     'tennet'
#     >>> greatest_pal_two("abc")
#     'a'
#     >>> greatest_pal_two("")
#     ''
#     """
#     for _____ in __________________________________________________________:
#         if ________________________________________________________________________:
#             return  ________________________________________________________________________
#     return s

