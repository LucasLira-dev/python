# c = 1

# while c < 11:
#     print(c)
#     c += 1
# print('FIM')

# n = 0

# while n != 7:
#     n = int(input('Digite um número: '))
# print('FIM')

c = 1
pares = 0
impares = 0

while c != 0:
    c = int(input('Digite um número: '))
    if c != 0:
        if c % 2 == 0:
            pares += 1
        else:
            impares += 1
print(f'''
A quantidade de Pares foi: {pares}
A quantidade de Impares foi: {impares}
''')