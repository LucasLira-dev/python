sequencia = int(input('Quantos termos da sequencia de Fibonacci voce quer ver? '))

num0 = 0
num1 = 1
c = 3

print(num0)
print(num1)
while c <= sequencia:
    fibonacci = num0 + num1
    print(f'{fibonacci}')
    num0 = num1
    num1 = fibonacci
    c += 1
print('FIM')
