num = int(input('Digite um número: '))
c = num - 1
fatorial = 0

while c > 1:
    c = c - 1
    num += num * c
    fatorial = num
print(f'o fatorial é: {fatorial}')