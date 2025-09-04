galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite a idade: ')))
    galera.append(dado[:])
    dado.clear()

print('-----------------------')

for pessoa in galera:
    if pessoa[1] >= 18:
        print(f' {pessoa[0]} é adulto')
    else:
        print(f' {pessoa[0]} não é adulto')