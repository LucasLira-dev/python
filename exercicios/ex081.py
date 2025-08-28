res = ''
valores = []

while res != 'N':
    num = int(input('Digite um numero: '))
    valores.append(num)
    res = input('Quer continuar? [S/N] ').upper()

valores.sort(reverse=True)

print(f'Quantidade de numeros digitados: {len(valores)}')
print(valores)

if 5 in valores:
    print('O número 5 está na lista')
else:
    print('O Numero 5 nao esta na lista')

