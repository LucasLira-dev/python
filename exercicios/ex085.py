numeros = list()
pares = list()
impares = list()


for c in range(0,7):
    num = int(input('Digite um número para adicionar na lista: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    
numeros.append(pares[:])
numeros.append(impares[:])

numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram {numeros[0]}')
print(f'Os valores impares digitados foram {numeros[1]}')