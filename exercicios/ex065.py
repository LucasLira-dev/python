media = 0
maior = 0
menor = 0
quantidade = 0
res = "S"
soma = 0

while res != "N":
    num = int(input('Digite um numero: '))
    soma += num
    if num > maior:
        maior = num
    if quantidade == 0:
        menor = maior
    if menor > num:
        menor = num 
    quantidade += 1
    print(num)
    res = input('''
        quer continuar?
        [S] - SIM
        [N] - NÃO
        ''').upper()
print(f'o maior valor foi: {maior}')
print(f'o menor valor foi: {menor}')
print(f'quantidade de numeros digitados: {quantidade}')
print(f'a média entre os números foi {soma/quantidade}')