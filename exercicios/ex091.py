from random import randint
from time import sleep
from operator import itemgetter

dadosJogadores = {
    'jogador1': 0 ,
    'jogador2': 0 ,
    'jogador3':  0,
    'jogador4':  0,
}

for k in dadosJogadores:
    dadosJogadores[k] = randint(1, 6)

for k, v in dadosJogadores.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)

ranking = sorted(dadosJogadores.items(), key=itemgetter(1), reverse=True) #lista os elementos na ordem inversa

colocacao = 1
print('Ranking final dos jogadores: ')
for c in ranking:
    print(f'{colocacao}ª lugar: {c[0]} com {c[1]}')
    colocacao += 1