
maior = 0
menor = 99999999

for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor: 
        menor = peso
print(f'o maior peso foi: {maior}')
print(f'o menor peso foi: {menor}')