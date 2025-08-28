valores = []

for c in range(0, 4):
    num = int(input('Digite um valor: '))
    pos = 0
    while pos < len(valores):
        if num <= valores[pos]:
            break
        pos +=1
    valores.insert(pos, num)
    print(f'Valor adicionado na posição {pos}')     
print(valores)