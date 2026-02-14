# Python dictionaries (dict type)
# Dictionaries are data structures of the type
# "key" and "value" pair.
# Keys can be considered as the "index"
# that we saw in the list and can be of immutable types
# such as: str, int, float, bool, tuple, etc.
# The value can be of any type, including another
# dictionary.
# We use the curly braces - {} - or the dict class to create
# dictionary.
# immutable: str, int, float, bool, tuple
# mutable: dict, list
# person = {
#     'first_name': 'Rogers Lucas',
#     'last_name': 'Damaceno',
#     'age': 18,
#     'height': 1.7,
#     'addresses': [
#         {'street': 'such and such', 'number': 123},
#         {'street': 'another street', 'number': 321},
#     ]
# }
# person = dict(first_name='Rogers Lucas', last_name ='Damaceno')

person = {
     'first name': 'Rogers Lucas',
     'last name': 'Damaceno',
     'age': 18,
     'height': 1.7,
     'addresses': [
         {'street': 'such and such', 'number': 123},
         {'street': 'another street', 'number': 321},
     ],
 }
print(person['first name'])
print(person['last name'])

print()

for keys in person:
    print(keys, person[keys])