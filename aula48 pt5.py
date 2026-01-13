'''
Be careful with mutable data
= - copied value (immutable)
= - points to the same value in memory (mutable) 

'''

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'anything'
print(lista_a)
print(lista_b)