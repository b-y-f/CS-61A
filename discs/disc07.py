class Student:

    max_slip_days = 3 # this is a class variable

    def __init__(self, name, staff):
        self.name = name # this is an instance variable
        self.understanding = 0
        staff.add_student(self)
        print("Added", self.name)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:

    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

    def grant_more_slip_days(self, student, days):
        student.max_slip_days = days

def test_Q1():
    """
    >>> callahan = Professor("Callahan")
    >>> elle = Student("Elle", callahan)
    Added Elle
    >>> elle.visit_office_hours(callahan)
    Thanks, Callahan
    >>> elle.visit_office_hours(Professor("Paulette"))
    Thanks, Paulette
    >>> elle.understanding
    2
    >>> [name for name in callahan.students]
    ['Elle']
    >>> x = Student("Vivian", Professor("Stromwell")).name
    Added Vivian
    >>> x
    'Vivian'
    >>> [name for name in callahan.students]
    ['Elle']
    >>> elle.max_slip_days
    3
    >>> callahan.grant_more_slip_days(elle, 7)
    >>> elle.max_slip_days 
    7
    >>> Student.max_slip_days
    3
    """


# Q2 Keyboard
class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0

class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.
    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) # No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """
    def __init__(self, *args):
        self.buttons = {}
        for b in args:
            self.buttons[b.pos] = b

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output."""
        if info in self.buttons:
            btn = self.buttons[info]
            btn.times_pressed += 1
            return btn.key
        return ''

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output."""
        output = ''
        for key in typing_input:
            output += self.press(key)
        return output


#  Q3: Cat

class Pet:

    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):

    def talk(self):
        super().talk()
        print('This Dog says woof!')


class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        self.is_alive = True
        self.name = name
        self.owner = owner
        self.lives = lives

    def talk(self):
        """Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        "*** YOUR CODE HERE ***"
        print(self.name + ' says meow!')


    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero,
        is_alive becomes False. If this is called after lives has
        reached zero, print 'This cat has no more lives to lose.'

        >>> dead_cat = Cat('Thomas', 'Tammy')
        >>> dead_cat.lives
        9
        >>> dead_cat.lose_life()
        >>> dead_cat.lives
        8
        >>> dead_cat.lose_life()
        >>> dead_cat.lives
        7
        """
        "*** YOUR CODE HERE ***"
        if self.lives == 0:
            print('This cat has no more lives to lose.')
        self.lives -= 1


# Q4: NoisyCat

class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""
    # def __init__(self, name, owner, lives=9):
    #     # Is this method necessary? Why or why not?
    #     "*** YOUR CODE HERE ***"


    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        "*** YOUR CODE HERE ***"
        super().talk()
        super().talk()


# Q5: Cat Adoption

import random as random

class CatRandomName(Pet):
    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner)
        self.lives = lives

    # Insert other previously defined methods here

    @classmethod
    def adopt_random_cat(cls, owner):
        """
        Returns a new instance of a Cat with the given owner,
        a randomly chosen name and a random number of lives.
        >>> randcat = CatRandomName.adopt_random_cat("Ifeoma")
        >>> isinstance(randcat, CatRandomName)
        True
        >>> randcat.owner
        'Ifeoma'
        """
        randName = random.choice(['DogA','DogB'])
        randLive = random.randint(0,99)
        return cls(randName, owner, randLive)


# Q6: WWPD: Repr-esentation
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

def testQ6():
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
