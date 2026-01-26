import random   # 



cpf = ''

for i in range(9):
    cpf += str(random.randint(0,9))


count_regressive = 10

result = 0

for digit in cpf:
    result += (int(digit)  * count_regressive)
    count_regressive -= 1

digit = ((result * 10) % 11)
digit = digit if digit <= 9 else 0


# part 2  
cpf_2 = cpf + str(digit)

count_regressive_1 = 11

result_1 = 0

for digit_1 in cpf_2:
    result_1 += (int(digit_1) * count_regressive_1)
    count_regressive_1 -= 1

digit_1 = ((result_1 * 10) % 11)
digit_1 = digit_1 if digit_1 <= 9 else 0

cpf_3 = cpf_2 + str(digit_1)

print(cpf_3)
