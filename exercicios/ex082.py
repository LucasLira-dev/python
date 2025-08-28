res = ''
valores = []
pares = []
impares = []

while res != 'N':
    num = int(input('Digite um valor: '))
    valores.append(num)
    res = input('Quer continuar? [S/N] ').upper()

for num in valores:
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 == 1:
        impares.append(num)

print(f'Lista completa: {valores}')
print(f'Lista de pares: {pares}')
print(f'Lista de impares: {impares}')

