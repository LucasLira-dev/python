r1 = int(input('Digite o comprimento da rota 1: '))
r2 = int(input('Digite o comprimento da rota 2: '))
r3 = int(input('Digite o comprimento da rota 3: '))

if (r1 + r2 ) > r3 and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('As rotas formam um triângulo.')
else:
    print('As rotas não formam um triângulo.')