'''
Lists in python
Type list - Mutable
Support multiple value of any type
Knowledge reusable - indexes and slicing
useful methods: 
    append - Add an item to the end
    insert - Add an item at the chosen index
    pop - Remove from the end or chosen index
    del - Delete an index
    clear - Clear the list
    extend - Ext end the list
    + - Concatenate lists

Create, Read, Update, Delete  = lista [i] (CRUD)

'''

lista = [10, 20, 30, 40]
lista.append('Rogers')
nome = lista.pop()
lista.append(1233)
del lista[-1]
lista.insert(100, 5)
# lista.clear()
print(lista)
# print(lista, nome)
