# Values Truthy and Falsy, mutable and immutable types
# Mutables [] {} set ()
# Immutable () "" 0 0.0 None False range (0, 10)

lists = []
dictionary = {}
sets = set()
tuples = ()
string = ''
whole = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def falsy(value):
    return 'falsy' if not value else 'truthy'

print(f'TESTE', falsy('TESTE'))
print(f'{lists=}', falsy(lists))
print(f'{dictionary=}', falsy(dictionary))
print(f'{sets=}', falsy(sets))
print(f'{tuples=}', falsy(tuples))
print(f'{string=}', falsy(string))
print(f'{whole=}', falsy(whole))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))