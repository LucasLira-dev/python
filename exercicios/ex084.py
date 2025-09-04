dadosPessoas = list()
dado = list()
pessoasPesadas = list()
pessoasLeves = list()

res= ''
totalPessoas = 0


while res != 'N':
    dado.append(str(input('Digite um nome: ')))
    dado.append(int(input('Digite o peso: ')))
    dadosPessoas.append(dado[:])
    dado.clear()
    totalPessoas += 1
    res = str(input('Quer continuar? [S/N]: ')).upper()

for pessoa in dadosPessoas:
    if pessoa[1] >= 100:
        dado.append(pessoa[0])
        dado.append(pessoa[1])
        pessoasPesadas.append(dado[:])
        dado.clear()
    elif pessoa[1] <= 70:
        dado.append(pessoa[0])
        dado.append(pessoa[1])
        pessoasLeves.append(dado[:])
        dado.clear()

print('------Total de pessoas cadastradas------')
print(totalPessoas)

print('------Lista de mais pesados------')
for pss in pessoasPesadas:
    print(f'{pss[0]} com {pss[1]} Kg')

print('------Lista de mais leves------')
for pss in pessoasLeves:
    print(f'{pss[0]} com {pss[1]} Kg')
