   # Introduction to the lambda fuction (one-line anonymous fuction)
   # The lambda fuction is a function like any
   # Other in Python. However, they are anonymous fuctions
   # Which contain only one line. In other words, everthing
   # Must be contained within a single 
   # Expression.

   # lists = [
   #   {'nome': 'Luiz', 'sobrenome': 'miranda'},
   #   {'nome': 'Maria', 'sobrenome': 'Oliveira'},
   #   {'nome': 'Daniel', 'sobrenome': 'Silva'},
   #   {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
   #   {'nome': 'Aline', 'sobrenome': 'Souza'},
   # ]

   # lista = [12, 1, 2, 54, 10, 24, 124, 22,]
   # lista.sort(reverse=True)
   # print(lista)

lists = [
      {'nome': 'Luiz', 'sobrenome': 'miranda'},
      {'nome': 'Maria', 'sobrenome': 'Oliveira'},
      {'nome': 'Daniel', 'sobrenome': 'Silva'},
      {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
      {'nome': 'Aline', 'sobrenome': 'Souza'},
   ]

   #def order(item):
   #    return item['nome']

   #lists.sort(key=order)

#lists.sort(key=lambda item: item['nome']) # Same thing as above, only this time using the lambda function

#for item in lists:
#   print(item)

def amostration(lists):
    for item in lists:
        print(item)
      

l1 = sorted(lists, key=lambda item: item['nome'])
l2 = sorted(lists, key=lambda item: item['sobrenome'])

amostration(l1)
print()
amostration(l2)