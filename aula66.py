'''
Named and unnamed arguments in python functions
Named argument has name with equal sign
Unnamed argument receives only the argument (value)
'''
# Definition
def soma(x, y, z):
    print(f'{x=} y={y} {z=}',  '|',   'x + y + z = ', x + y + z)

soma(1, 2, 3)
soma(y=2, z=3 ,x=1)

print(1, 2, 3, sep='-')
