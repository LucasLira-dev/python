dados = list()
gols = list()
total = 0

while True:
    jogador = dict()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    
    jogador['gols'] = gols
    gols = []  
    total_jogador = 0
    for c in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {c+1} ? '))
        gols.append(gol)
        total_jogador += gol
    jogador['gols'] = gols[:]
    jogador['total'] = total_jogador
    dados.append(jogador)
    total += total_jogador
    while True: 
        res = str(input('Quer continuar? [S/N]: ')).upper()
        if res == 'SN':
            break
            print('ERRO! Responda com S ou N ')
    if res == 'N':
        break


print('-'*40)
print(f'{'Índice':<7}{'Nome':<15}{'Gols':<15}{'Total':<7}')
print('-'*40)
for i, jogador in enumerate(dados):
    print(f'{i:<7}{jogador['nome']:<15}{str(jogador['gols']):<15}{jogador['total']:<7}')
print('-'*40)


while True: 
    jogo = 1
    ind = int(input('Quer ver os dados de qual jogador? (999 FINALIZA) '))
    if ind == 999:
        break
    if ind < 0 or ind >= len(dados):
        print(f'ERRO! Não existe jogador com o indice {ind} ')
        continue
    print(f'---LEVANTAMENTO DE DADOS DO JOGADOR {dados[ind]['nome']}')
    for c in dados[ind]['gols']:
        print(f'no jogo {jogo} ele fez {c} gols')
        jogo += 1

