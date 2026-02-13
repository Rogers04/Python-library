'''
(Closure) and function that returns other functions
'''

'''
def create_saudation(saudation, name):
    def greet():
        return f'{saudation}, {name}'
    return greet

s1 = create_saudation('Good Morning', 'Rogers')
s2 = create_saudation('Good Night', 'Menina')

print(s1())
print(s2())
'''


def create_saudation(saudation):
    def greet(name):
        return f'{saudation}, {name}'
    return greet



speak_good_morning = create_saudation('Good Morning')
speak_good_night = create_saudation('Good Night')

for name in ['Rogers', 'Maria', 'João']:
    print(speak_good_morning(name))

print('---'*25)

for name in ['Menina ', 'Menina 2', 'Menina 3', 'Menina 4']:
    print(speak_good_night(name))
    