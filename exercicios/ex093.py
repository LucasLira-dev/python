dados = {}
gols = []
total = 0

dados['nome'] = str(input('Nome do jogador: '))

partidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))

for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1} ? ')))
dados['gols'] = gols

for c in dados['gols']:
    total += c
dados['total'] = total

for k, v in dados.items():
    print(f'{k} = {v}')

print(f'o jogador {dados["nome"]} fez {partidas} partidas.')

for i, v in enumerate(dados['gols']):
    print(f'=> na partida {i+1} ele fez {v} gols')

print(f'No total ele fez {dados["total"]} gols')