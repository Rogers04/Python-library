nome = 'Rogers Lucas Damaceno'
altura = 1.70
peso = 60
imc = peso / (altura*altura)

linha_1 = f'{nome} tem {altura:.2f} de altura pesa {peso} quilos, e seu IMC é: {imc}'

print(linha_1)

# Nessa linha_1 aprendemes que se colocarmos a letra 
# f depois do = ela transforma a variável em uma f-string
# nos possibilitando fazer o uso de frases e outras variáveis juntas
# Esse 2f que colocamos em altura serve para ele ler o número zero
# assim ele irá ler duas casas decimais