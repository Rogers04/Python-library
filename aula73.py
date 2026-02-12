'''
Higher Order Functions
'''

def saudation(msg, name):
    return f'{msg}, {name}'

def execute(function, *args):
    return function(*args)

print(
    execute(saudation,'Good morning', 'Rogers')
)

print(
    execute(saudation, 'Good night', 'menina')
    )