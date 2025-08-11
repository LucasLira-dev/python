r1 = int(input('Digite o comprimento da rota 1: '))
r2 = int(input('Digite o comprimento da rota 2: '))
r3 = int(input('Digite o comprimento da rota 3: '))

if (r1 + r2 ) > r3 and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('As rotas formam um triângulo.')
    if r1==r2 and r2==r3:
        print('Todos os lados são iguais, o que forma um triangulo EQUILÁTERO')
    elif r1==r2 or r1==r3 or r2 ==r3:
        print('Dois lados são iguais, o que forma um triangulo ISOSCELES')
    elif r1 != r2 and r1 != r3:
        print('Todos os lados são diferentes, o que forma um triangulo ESCALENO')
else:
    print('As rotas não formam um triângulo.')