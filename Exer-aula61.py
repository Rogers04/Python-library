"""
Calculation of the first digit of the CPF
CPF: 746.824.890-70
Collect the sum of the first 9 digits of the CPF
multiplying each of the values by a
countdown starting from 10




Ex.: 746.824.890-70 (746824890)
10 9 8 7 6 5 4 3 2
 7 4 6 8 2 4 8 9 0
70 36 48 56 12 20 32 27 0




Add all the results:




70+36+48+56+12+20+32+27+0 = 301
Multiply the previous result by 10
301 * 10 = 3010
Obtain the remainder of the division of the previous account by 11
3010 % 11 = 7
If the previous result is greater than 9:
result is 0
opposite of this:
result is the amount of the account




The first digit of the CPF is 7
"""


cpf = input('Enter you cpf: ')

nine_digit = cpf[:9]
count_regressive = 10

result = 0

for digit in nine_digit:
    result += (int(digit)  * count_regressive)
    count_regressive -= 1

digit = ((result * 10) % 11)
digit = digit if digit <= 9 else 0


# part 2  
cpf_2 = nine_digit + str(digit)

count_regressive_1 = 11

result_1 = 0

for digit_1 in cpf_2:
    result_1 += (int(digit_1) * count_regressive_1)
    count_regressive_1 -= 1

digit_1 = ((result_1 * 10) % 11)
digit_1 = digit_1 if digit_1 <= 9 else 0

cpf_3 = cpf_2 + str(digit_1)


if cpf == cpf_3:
    print(f'You cpf {cpf_3} is valid')
else:
    print('Invalid')