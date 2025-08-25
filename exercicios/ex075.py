nums = []

for c in range(0,4):
    num = int(input('Digite um número: '))
    nums.append(num)
tupla = tuple(nums)

print(f'O número 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O número 3 foi encontrado na posição {tupla.index(3)+1}')
else:
    print('O número 3 não está presente na tupla')

print('Numeros pares presentes: ')
for c in tupla:
    if c % 2 == 0:
        print(c)