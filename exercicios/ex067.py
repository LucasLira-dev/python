num = 0

while True:
    print('----------------------------')
    num = int(input('QUER VER A TABOADA DE QUAL VALOR? '))
    if num <= 0:
        break
    cont = 1
    while cont <= 10:
        print(f'{num} x {cont} = {num*cont}')
        cont += 1
print('----------------------------')
print('FIM DE PROGRAMA')