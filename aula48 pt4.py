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
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)

print(lista_a, 'Using extend')
print(lista_c, 'Using concatenate')