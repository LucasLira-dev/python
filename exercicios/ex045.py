import random

print('-------- JOKENPO -------')

humano = int(input('''
Faça sua escolha:
1 - PEDRA
2 - PAPEL
3 - TESOURA
'''))

computador = random.randint(1, 3)

if humano == 1 and computador == 2:
    print('O computador venceu!')
elif humano == 1 and computador == 3:
    print('AEEEEEEEEEEE! voce venceu!')
elif humano == 2 and computador == 3:
    print('O computador venceu.....')
elif humano == 2 and computador == 1:
    print('AEEEEEEEEEEE! voce venceu!')
elif humano == 3 and computador == 1:
    print('O computador venceu.....')
elif humano == 3 and computador == 2:
    print('AEEEEEEEEEEE! voce venceu!')