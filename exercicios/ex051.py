print('-----PROGRESSÃO-ARITMETICA-----')
primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

print('Os 10 primeiros termos dessa progressão são: ')
for c in range(0, 10):
    termo = primeiroTermo + razao * c
    print(termo)
print('FIM')