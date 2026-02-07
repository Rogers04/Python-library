# Exercise with functions 

'''

Create a function that multiples all the unmaded arguments it receives.
Returns the total to a variable and displays the value of the variable.
'''

def soma(*args):
    total = 1

    for number in args:
        total *= number

    return total    
    
mult = soma(1,2,3,4,5)

print(mult)


print('-#-'*25)
'''

Creates a function that tells whether a number is even or odd.
returns wheter is even or odd.
'''
 


def pi(a = int):
    
    if a % 2 == 0:
        print('Number is even')
    elif a % 2 != 0:
        print('Number is odd')
    else: 
        print('Error')

pi(2.0)