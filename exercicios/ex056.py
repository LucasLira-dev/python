
oldMan = 'a'
idadeHomem = 0
newWomen = 0
totalAnos = 0
media = 0

for c in range(0, 4):
    print('-----------------------')
    nome = input('Digite um nome: ')
    sexo = int(input('''Digite seu sexo:
    [1] HOMEM
    [2] MULHER 
    '''))
    idade = int(input('Digite sua idade: '))
    print('-----------------------')
    totalAnos += idade
    if sexo == 1:
        if idade > idadeHomem:
            idadeHomem = idade
            oldMan = nome
    elif sexo == 2 and idade < 20:
        newWomen += 1
media = totalAnos / 4
print(f'o homem mais velho é o: {oldMan} com {idadeHomem} anos')
print(f'a quantidade de mulheres com menos de 20 anos é: {newWomen}')
print(f'A média de idade é: {media} anos')
