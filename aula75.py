'''
Exercices

Create function that doubles, triples and quadruples
the number received as a parameter
'''


def creat_multplicator(mult):
    def multiply(number):
        return number * mult
    return multiply

double = creat_multplicator(2)
triples = creat_multplicator(3)
quadruples = creat_multplicator(4)


print(double(2))
print(triples(3))
print(quadruples(4))

