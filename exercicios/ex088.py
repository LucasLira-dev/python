import random
from time import sleep

print('-------------------------')
print('JOGO DA MEGA-SENA')
print('-------------------------')

jogos = list()

qntdJogos = int(input('Quantos jogos oce quer gerar?: '))

for c in range(0, qntdJogos):
    lista = list()
    for c in range(0, 6):
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
    jogos.append(lista[:])  

c = 1
for jogo in jogos:
    sleep(2)
    print(f'JOGO Nº {c}: {jogo}')
    c +=1
    