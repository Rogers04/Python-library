'''
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
'''

'''text = iter('Rogers')   # __iter__()

print(next(text))
print(next(text))
print(next(text))
print(next(text))
print(next(text))
print(next(text))

print(next(text))
'''

text = 'Rogers'
'''
iteratador = iter(text)

while True:
    try:
        letter = next(iteratador)
        print(letter)
    except StopIteration:
        break'''

# Instead of writing a long code 
# like the one above we can just use 'for'

for letter in text:
    print(letter)