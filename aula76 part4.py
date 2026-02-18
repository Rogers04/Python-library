'''
Useful methods of dictionaries in Python
len - how many keys
keys - iterable over keys
values - iterable over keys and values
setdefault - add value if key does not exist
copy - return a (shallow copy)
get - get a key
pop - delete an item with the specified key (del)
popitem - delete the last item added
update - update a dictionary with another
'''
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'li': [0, 1, 2],
}

d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['li'][1] = 999999

print(d1)
print(d2)