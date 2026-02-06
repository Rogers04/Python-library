'''
args - argumentos não nomeados
* - * args (empacotamento e desempacotamento)
'''
'''
x, y, *resto = 1, 2, 3, 4
print(x, y, resto )


def soma (*args):
    total = 0
#   args = list(args)


    for number in args:
        print('Total', total, number)
        total += number
        print('Total', total)




soma(1, 2, 3, 4, 5, 6)
'''


x, y, *resto = 1, 2, 3, 4
print(x, y, resto )


def soma (*args):
    total = 0


    for number in args:
        total += number
    return total


soma_1_2_3 = soma(1, 2, 3 )
#print(soma_1_2_3)


soma_4_5_6 = soma (4, 5, 6)
#print(soma_4_5_6)


numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
other_soma = soma(*numbers)
print(other_soma)


print(sum(numbers))

