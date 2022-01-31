from os import path
import re


class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
         return self.x

    def __str__(self):
         return self.x * 2

class B:
    def __init__(self):
         print('boo!')
         self.a = []

    def add_a(self, a):
         self.a.append(a)

    def __repr__(self):
         print(len(self.a))
         ret = ''
         for a in self.a:
             ret += str(a)
         return ret

def testQ1():
    """
    >>> A('one')
    one
    >>> print(A('one'))
    oneone
    >>> repr(A('two'))
    'two'
    >>> b = B()
    boo!
	>>> b.add_a(A('a'))
	>>> b.add_a(A('b'))
	>>> b
	2
	aabb
    """


class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


# Q2: The Hy-rules of Linked Lists

ganondorf = Link('zelda', Link('link', Link('sheik', Link.empty)))

def testQ2():
	"""
	>>> ganondorf.rest.rest.first
	'sheik'
	>>> ganondorf.rest.first
	'link'
	>>> str(ganondorf)
	'<zelda link sheik>'
	>>> ganondorf.rest.first = 'ganondorf'
	>>> str(ganondorf)
	'<zelda ganondorf sheik>'
	"""

# Q3: Sum Nums
def sum_nums(s):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    "*** YOUR CODE HERE ***"
    if s.rest is Link.empty:
        return s.first
    return sum_nums(s.rest) + s.first

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Implementation Note: you might not need all lines in this skeleton code
    res = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        res *= lnk.first
    rest_lst = [i.rest for i in lst_of_lnks]
    return Link(res, multiply_lnks(rest_lst))
        
def flip_two(s):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    "*** YOUR CODE HERE ***"
    if s is Link.empty or s.rest is Link.empty:
        return
    s.first, s.rest.first = s.rest.first, s.first
    flip_two(s.rest.rest)


class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches


def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    >>> t.branches[2].label
    6
    """
    "*** YOUR CODE HERE ***"
    if t.label % 2!= 0:
        t.label += 1
    for b in t.branches:
        make_even(b)

def leaves(t):
    """Returns a list of all the labels of the leaf nodes of the Tree t.

    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    "*** YOUR CODE HERE ***"
    res = []
    if t.is_leaf():
        return [t.label]
    for b in t.branches:
        res += leaves(b)
    return res




# def find_paths(t, entry):
#     """
#     >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
#     >>> find_paths(tree_ex, 5)
#     [[2, 7, 6, 5], [2, 1, 5]]
#     >>> find_paths(tree_ex, 12)
#     []
#     """