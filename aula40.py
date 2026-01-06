# Calculator #


while True:
   
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operators = input('Digite um operador (+-*/): ')


    number_valid = None


#----------------------------------- Convertion of Int for Float -------------------------#
# We only use (try) and (except) because we are learning, and so the code doesn't break
 
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        number_valid = True


    except:
        number_valid = None
#-----------------------------------------------------------------------------------------------#


    if number_valid is None:
        print('Number invalid. Please correct')
        continue
   
    allowed_operators = '+-*/'


    if operators not in allowed_operators:
        print('Invalid operators')
        continue            # We use (continue) to 'restart' the while in the part that went wrong
   
    if len(operators) > 1:
        print('Enter only one operator')
        continue


#------------------------------------------------------- Calculator System ---------------------------------------------------#
    if operators == '+':
        print(f'{num1_float} + {num2_float} =', num1_float + num2_float)
   
    if operators == '-':
        print(f'{num1_float} - {num2_float} =', num1_float - num2_float)
       
    if operators == '*':
        print(f'{num1_float} * {num2_float} =', num1_float * num2_float)


    if operators == '/':
        print(f'{num1_float} / {num2_float} =', num1_float / num2_float)
   


#----------------------------------------------------- System of program exit ------------------------------------------------#


    exit = input('Do you want leave? [Y]es: ').lower().startswith('y')


    if exit is True:
        break


