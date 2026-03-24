# Packing and unpacking of dicionary


'''
(a1, a2), (b1, b2) = people.items()
#print(a1, a2)
#print(b1, b2)

for key, value in people.items():
    print(key, value)'''


a, b = 1, 2
a, b = b, a
print(a, b)

people = {
    'nome': 'Rogers',
    'sobrenome': 'Lucas',
}

data_people = {
    'age': 18,
    'height': 1.7,
}

complet_people = {**people, ** data_people}
#print(complet_people)


def show_named_arguments(*args, **kwargs):
    print('Not named:', args)

    for key, value in kwargs.items():
        print(key, value)

#show_named_arguments(**complet_people)

# args and kwargs
# kwargs - keyword arguments

configuration = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
    
show_named_arguments(**configuration)