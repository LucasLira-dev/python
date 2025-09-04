numeros = list()
soma = 0
soma3coluna = 0

for i in range(0, 3):
    lista = list()
    for j in range(0, 3):
        lista.append(int(input(f'Digite um número para a posição [{i}][{j}]')))
    numeros.append(lista[:])

print('-------------------------')
for linha in numeros:
    for valor in linha: 
        print(f'{valor} | ', end='')
        if valor % 2 == 0:
            soma += valor
    print()  # Adiciona quebra de linha após cada linha
maior2linha = max(numeros[1])

for linha in range(0, 3):
    soma3coluna += numeros[linha][2]

print('-------------------------')
print(f'A soma total de pares presentes na lista é: {soma}')
print(f'o maior numero da segunda linha foi: {maior2linha}')
print(f'a soma da terceira coluna foi: {soma3coluna}')

