boletim = list()

res = ''

c = 0

while res != 'N':
    dado = list()
    nome = list()
    notas = list()
    nomeAluno = input('Digite o nome do aluno: ')
    nome.append(nomeAluno)
    dado.append(nome)
    firstNote = float(input(f' Digite a primeira nota do {nomeAluno}: '))
    notas.append(firstNote)
    secondNote = float(input(f' Digite a segunda nota do {nomeAluno}: '))
    notas.append(secondNote)
    dado.append(notas)
    boletim.append(dado)
    res = str(input('Quer continuar? [S/N]: ')).upper()

for dados in boletim:
    nome = dados[0][0]
    notas = dados[1]
    media = (notas[0]+notas[1])/2
    print(f'o aluno Nª{c} teve a média {media}')
    c += 1

resp = 0

while resp != 999:
    resp = int(input('Quer ver as notas de algum aluno? (999 INTERROMPE)  '))
    if resp >= 0 and resp < len(boletim):
        aluno = boletim[resp][0][0]
        notas = boletim[resp][1]
        print(f'as notas de {boletim[0][0]} foram: {notas}')
    else:
        print('Opçao invalida')
