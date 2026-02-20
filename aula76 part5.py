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
p1 = {
    'first name': 'Rogers Lucas',
    'last name': 'Damaceno',
} 

#print(p1['first name'])
#print(p1.get('first name', 'Does not exist'))


#       Delete the first name
#name = p1.pop('first name')
#print(name)
#print(p1)

#       Delete the final name
#final_key = p1.popitem()
#print(final_key)
#print(p1)

#p1.update({
#    'first name':'new value',
#    'age': 18,
#})
#print(p1)

#p1.update(first_name= 'new value', age= 18)

#tupla = ('first name', 'new value'), ('age', 18)
lista = [['first name', 'new value'], ['age', 18]]
p1.update(lista)
print(p1)