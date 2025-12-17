a = 'A'
b = 'B'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'

formato =string.format(nome1=a, nome2=b, nome3=c)

print(formato)

# Dessa forma usando o nome1.2.3 tem suas vantagens
# pois vc não precisa ficar dependendo da ordem do format
# então facilitado o seu controle
# essa é uma das única maneiras para vc controlar essa ordem 