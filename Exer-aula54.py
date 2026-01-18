'''
Make a shopping list with lists the user must be able to insert, delete and list 
values from his list. Do not allow the program to break with errors of non-existent
indexes in the list.
'''
import os

lista =[]

# ---------------------------------------------------------------------------------------- #

while True:
    selection = input('Select one of these options: [I]nsert, [D]elete, [L]ist: ')
    
    if selection == 'I' or selection == 'i':
        os.system('cls')
        value = input('Enter: ')
        lista.append(value)


# ---------------------------------------------------------------------------------------- #

    elif selection == 'D' or selection == 'd':
        ind_str = input('Choice the index for delet: ')

        try:
            indice = int(ind_str)
            del lista[indice]
        
        except IndexError:
            print('Index does not exist in the list')
        except ValueError:
            print('Please number type one int')
        except Exception:
            print('Error Unknown')


# ----------------------------------------------------------------------------------------- #
    elif selection == 'L' or selection == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nothing for list')
        
        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print('Please type the value: I, D or L')