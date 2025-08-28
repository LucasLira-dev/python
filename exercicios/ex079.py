valores = []
res = ''


while res != 'N':
    num = int(input('Digite um número: '))
    if num in valores:
        print('Este número ja foi adicionado anteriormente......')
    else:
        valores.append(num)
    res = input('Quer continuar? [S/N] ').upper()
valores.sort()
print(f'Voce digitou os valores {valores}')