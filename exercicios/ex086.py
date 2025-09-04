matriz = list()

for i in range(0, 3):
    lista = list()
    for j in range(0, 3):
        lista.append(int(input(f'Digite um número para a posição [{i}][{j}]: ')))
    matriz.append(lista[:])


print('------------------------')
for linha in matriz:
    for valor in linha: 
        print(f'{valor} | ', end='')
    print()  # Adiciona quebra de linha após cada linha