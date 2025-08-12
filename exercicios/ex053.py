frase = str(input('Digite uma frase: ')).replace(' ', ' ').lower()

if frase == frase[::-1]:
    print('A frase é palíndroma!')
else:
    print('A frase não é palíndroma.')
