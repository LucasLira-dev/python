num = int(input('Digite um número: '))
total= 0

for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[32m{c}\033[m', end=' ')  # Verde para divisores
    else:
        print(f'\033[31m{c}\033[m', end=' ')  # Vermelho para não divisores '
for c in range(1, num+1):
    if num % c ==0:
        total+= c
if total > 2:
    print(' o numero não é primo')
else:
    print(' o numero é primo')