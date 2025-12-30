'''
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
'''

'''
Fiz isso para te mostrar que com esses tipos imutáveis
nós jamais conseguiriamos alterar eles. Vemos isso no exemplo abaixo,
onde que para alterar a Variável é preciso eu fazer a criação de uma nova
Variável, para assim eu poder mudar ela.
'''


string = 'Rogers Lucas'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)

print(outra_variavel)


# Busque sempre olhar a documentação dos códigos, não importando qual linguagem seja
