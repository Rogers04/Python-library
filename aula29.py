'''


Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar


'''


numero_str = input('Vou dobrar o número que vc digiitar: ')


'''
if numero_str.isdigit():
    numero_float = float(numero_str)    # Fazemos isso para converter a Var numero_str
                                        # para um float, se não, não irá funcionar
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')


else:
    print('Isso não é um número')
'''


try:
    print('STR:', numero_str)   # Estou fazendo isso para te mostrar que mesmo
                                # se o código for quebrar como no de cima
                                # ele não deixa e pula para o except


    numero_float = float(numero_str)    # Fazemos isso para converter a Var numero_str
                                        # para um float, se não, não irá funcionar
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')


except:
    print('Isso não é um número')

