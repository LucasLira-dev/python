from math import sqrt

cateto1 = int(input('Digite o comprimento do cateto 1: '))
cateto2 = int(input('Digite o comprimento do cateto 2: '))

hipotenusa = sqrt((cateto1**2) + (cateto2**2))

print(f'A hipotenusa é: {hipotenusa}')