quantidade = 0
soma = 0
num= 0

while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        soma += num
        quantidade += 1
print(f'foram digitados {quantidade} números e a soma total é: {soma}')