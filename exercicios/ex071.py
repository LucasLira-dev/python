valor = int(input('Quanto vc quer sacar?: '))
total50 = total20 = total10 = total1 = total = 0

while valor > 0:
    if valor >= 50:
        total50 = valor // 50
        valor = valor % 50
    elif valor >= 20:
        total20 = valor // 20
        valor = valor % 20
    elif valor >= 10:
        total10 = valor // 10
        valor = valor % 10
    else:
        total1 = valor // 1
        valor = valor % 1
print(f' quantidade de cédulas de 50 R$: {total50}')
print(f' quantidade de cédulas de 20 R$: {total20}')
print(f' quantidade de cédulas de 10 R$: {total10}')
print(f' quantidade de cédulas de 1 R$: {total1}')