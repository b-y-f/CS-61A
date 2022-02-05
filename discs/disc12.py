

"""
?start: select_statement
select_statement: "YOUR CODE HERE"
columns: "YOUR CODE HERE"
table: "YOUR CODE HERE"
condition: "YOUR CODE HERE"
COMPARATOR: "<" | ">" | "=" | ">=" | "<=" | "!="

%doctest
lark> SELECT name, age FROM cats
....> WHERE age > 3 AND lives > 5 AND tail = 1;
select_statement
  columns
    name
    age
  table  cats
  condition
    age
    >
    3
  condition
    lives
    >
    5
  condition
    tail
    =
    1
%end
%import common.WORD
%import common.NUMBER
%ignore /\s+/
"""



import re
def email_validator(email, domains):
    """
    >>> email_validator("oski@berkeley.edu", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@gmail.com", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@berkeley.com", ["berkeley.edu", "gmail.com"])
    False
    >>> email_validator("oski@berkeley.edu", ["yahoo.com"])
    False
    >>> email_validator("xX123_iii_OSKI_iii_123Xx@berkeley.edu", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@oski@berkeley.edu", ["berkeley.edu", "gmail.com"])
    False
    >>> email_validator("oski@berkeleysedu", ["berkeley.edu", "gmail.com"])
    False
    """
    pattern = ('^\w+@('+ '|'.join(domains) + ')').replace('.','\.')
    # print(pattern)
    return bool(re.search(pattern, email))
