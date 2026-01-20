# Unpacking in calls
# of methods and function

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'is', 'good'
salas = [ 
      # 0       1
    [ 'Maria', 'Helena', ],   # 0

      # 0
    ['Elaine', ], # 1
      
      #0       1       2
    ['Luiz', 'João', 'Eduarda',]#(0, 10, 20, 30, 40)],   # 2 
]


p, b, *_, ap, u = lista
print(p, u,ap)

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*lista)
print(*string)
print(*tupla)
print('\n', *salas, sep='\n')