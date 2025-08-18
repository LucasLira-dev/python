print('-----PROGRESSÃO-ARITMETICA-----')
primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
totalTermos = 10
qntd = totalTermos
c = 0

print('Os 10 primeiros termos dessa progressão são: ')
while c < totalTermos and qntd != 0:
    termo = primeiroTermo + razao * c
    print(termo)
    c += 1
    if c == totalTermos:
        qntd = int(input('Deseja ver mais quantos termos?: '))
        totalTermos += qntd
print('FIM')