def execut(function, *args):
    return function(*args) 
'''
def sum (x, y):
    return x + y

def creat_multiplication(mult):
    def multiplic(number):
        return number * mult
    return multiplic
'''

duplica = execut(
    lambda m: lambda n: n * m,
    2
)

print(duplica(2))


print(
    execut(
        lambda x, y: x + y,
        2, 3
    ),
)


print(
    execut(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)