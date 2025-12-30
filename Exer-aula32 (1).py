'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.




===================================================================================================



user = input('Digite um número inteiro: ')

entrada = input('Deseja converter para Número [S]im  [N]ão: ')
print(entrada)



if entrada == 'S' or entrada == 's':
    user_int = int(user)
   
    if user_int % 2 == 0:
        print('Esse número é PAR')
    
    if user_int % 2 != 0:
        print('Esse número é ÍMPAR')


elif entrada == 'N' or entrada == 'n':
    print('Só aceitamos números e isso é uma String')






'''



'''
Faça um programa que pergunte a hora ao usuário e, basendo-se no horário
descrito, exiba a saudação apropriada. Ex: Bom dia 0-11, Boa tarde 12-17
e Boa noite 18-23.


========================================================================================================


hora = input('Que horas são: ')
hora_int = int(hora)






if hora_int >= 0 and hora_int <= 11:
    print('Bom dia')


elif hora_int >= 12 and hora_int <= 17:
    print('Boa tarde')


elif hora_int >= 18 and hora_int <= 23:
    print('Boa noite')


'''




'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".



'''


first_name = input('Digite seu primeiro nome aqui: ')


contagem = len(first_name)


if contagem <= 4:
    print('Seu nome é curto')


elif contagem > 4 and contagem <= 6:
    print('Seu nome é normal')


elif contagem > 6:
    print('Seu nome é muito grande')
