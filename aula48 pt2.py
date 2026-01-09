'''
Lists in python
Type list - Mutable
Support multiple value of any type
Knowledge reusable - indexes and slicing
useful methods: 
    append, insert, pop, del, clear, extend, +
Create, Read, Update, Delete  = lista [i] (CRUD)

'''
#        0   1   2   3
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
last_value = lista.pop(3)
print(lista, 'Removido', last_value)

