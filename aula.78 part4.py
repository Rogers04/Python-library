# Sets - Sets in Python (set type)
# Sets are taught in mathematics
# Sets in Python are mutable, but accept only
# immutable types as internal values.


# Creating a set
# set(iterable) or {1, 2, 3}

# s1 = set('Rogers')
# s2 = {'Rogers', 1, 2, 3}
# print(s1)
# print(s2)

# s1 = set()  # Empty
# s1 = {'Rogers', 1, 2, 3}    # with data

# Sets are efficient for removing duplicate values
# from iterables.
# - They do not accept mutable values;
# - Their values ​​will always be unique;
# - They do not have indexes;
# - They do not guarantee order;
# - They are iterable (for, in, not in)

# li = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(li)
# l2 = list(s1)
# print(l2)

# s1 = {1, 2, 3}
# print(3 not in s1)


# for number in s1:
#    print(number)

# Useful methods:
# add, update, clear, discard

s1 = set()
s1.add('Rogers')
s1.add(1)
s1.update(('Hello Word', 1, 2, 3, 4))
# s1. clear()
s1.discard('Hello Word')
s1.discard('Rogers')
# print(s1)


# Useful operators:
# union | union - Joins
# intersection & - Items present in both
# difference - Items present only in the left set
# symmetric difference ^ - Items not in both

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2    # Union
s3 = s1 & s2    # Intersection
s3 = s1 - s2    # Difference
s3 = s2 - s1    # Difference
s3 = s1 ^ s2    # Symmetric difference

print(s3)