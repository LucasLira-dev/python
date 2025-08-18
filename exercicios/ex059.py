import time

res = 0
maior = 0

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

while res !=5:
    print('---------------')
    print('---OPERAÇOES---')
    res = int(input('''O que acontece agora?
    [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - MAIOR NÚMERO
    [4] - DIGITAR NOVAMENTE
    [5] - ENCERRAR  '''))
    if num2 > num1:
        maior = num2
    else:
        maior = num1
    if res == 1:
        print('---------------')
        print(f'a soma dos números é: {num1+num2}')
        print('---------------')
        time.sleep(2)
    elif res == 2:
        print('---------------')
        print(f'a multiplicação dos números é: {num1*num2}')
        print('---------------')
        time.sleep(2)
    elif res == 3:
        print('---------------')
        print(f'o maior numero foi: {maior}')
        print('---------------')
        time.sleep(2)
    elif res == 4:
        print('Digite os numeros novamente...')
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        time.sleep(2)
print('FIM')