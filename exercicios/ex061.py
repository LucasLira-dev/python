print('-----PROGRESSÃO-ARITMETICA-----')
primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
c = 0

print('Os 10 primeiros termos dessa progressão são: ')
while c < 10:
    termo = primeiroTermo + razao * c
    print(termo)
    c += 1
print('FIM')