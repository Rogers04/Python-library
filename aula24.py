# Operadores in e not in
# String são iteráveis, elas podem ser acessadas como itens
# 0 1 2 3 4 5
# R o g e r s
#-6-5-4-3-2-1
 
'''nome = 'Rogers'
print(nome[2])
print(nome[-3])
print(10 * '--')
print('gers' in nome)
print('as' in nome)'''


nome = input('Digite seu nome: ')
encontrar = input('Digite o que você deseja encontrar: ')


if encontrar in nome:
    print(f'{encontrar} está em {nome}')


else:
    print(f'{encontrar} não está em {nome}')

