dadosAlunos = {}

nome = str(input('Digite o nome do aluno: '))
dadosAlunos['Nome'] = nome

media = float(input(f' Digite a média de {nome}: '))
dadosAlunos['Media'] = media

if media >= 6:
    dadosAlunos['Situacao'] = 'Aprovado'
else:
    dadosAlunos['Situacao'] = 'Reprovado'

for k, v in dadosAlunos.items():
    print(f'{k} é igual a {v}')