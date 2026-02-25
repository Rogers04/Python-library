# Sets - Sets in Python (set type)
# Sets are taught in mathematics
# Sets in Python are mutable, but accept only
# immutable types as internal values.


# Creating a set
# set(iterable) or {1, 2, 3}

s1 = set('Rogers')
s2 = {'Rogers', 1, 2, 3}
print(s1)
print(s2)

#s1 = set()  # Empty
#s1 = {'Rogers', 1, 2, 3}    # with data

# Sets are efficient for removing duplicate values
# from iterables.
# - They do not accept mutable values;
# - Their values ​​will always be unique;
# - They do not have indexes;
# - They do not guarantee order;
# - They are iterable (for, in, not in)


# Useful methods:
# add, update, clear, discard

# Useful operators:
# union | union - Joins
# intersection & - Items present in both
# difference - Items present only in the left set
# symmetric difference ^ - Items not in both