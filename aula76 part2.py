# Manipulating keys and values in a dictionary

person = {}

##
##

keys = 'name'

person[keys] = 'Rogers Lucas'
person['last name'] = 'Damaceno'  

print(person[keys])


person[keys] = 'Felipe'

#del person['last name']
print(person)
print(person[keys])


if person.get('last name') is None:
    print('Does NOT exist')

else:
    print(person['last name'])