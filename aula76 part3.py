'''
Useful methods of dictionaries in Python

len - how many keys
key - iterable over keys
values - iterable over values
items - iterable over keys and values
setdefault - add value if key does not exist 
copy - return a shallow copy
get - get a key
pop - delet an item with the specified key (del)
popitem - delete the last item added
update - update a dictionary with another 
'''

person = {
    'first name': 'Rogers Lucas',
    'last name': 'Damaceno',
    'age': 18,
}

#print(len(person))

#print(list(person.keys()))
#for chave in person:
#    print(chave)

#print(list(person.values()))
for chave in person.values():
    print(chave)


#print(list(person.items()))
#for key, value in person.items():
#    print(key, value)

#person.setdefault('age',18)
#rint(person['age'])