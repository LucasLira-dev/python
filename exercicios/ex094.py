dados = list()
acimaMedia = list()

somaIdade = 0

while True:
    pessoas = dict()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('sexo: [M/F] ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    pessoas['idade'] = int(input('idade: '))
    dados.append(pessoas.copy())
    somaIdade += pessoas['idade']
    while True:
        res = str(input('Quer continuar?: [S/N] ')).upper()
        if res in 'SN':
            break
        print('ERRO! escolha S ou N')
    if res == 'N':
            break

mediaIdade = somaIdade / len(dados)

print(dados)
print(f'O grupo tem: {len(dados)} pessoas')
print(f'Média: {mediaIdade:3}')

print('Mulheres cadastradas: ')

for pessoa in dados:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'])
    if pessoa['idade'] > mediaIdade:
        acimaMedia.append(pessoa)

print('lista de pessoas acima da idade média: ')

for pessoa in acimaMedia:
    print(pessoa)
