maiores = homens = mulheresNovas = 0

while True:
    print('--------------------')
    print('CADASTRE UMA PESSOA')
    idade = int(input('Digite sua idade: '))
    sexo = input('SEXO: [M/F] ').strip().upper()
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheresNovas += 1
    print('--------------------')
    res = input('Quer continuar? [S/N] ').strip().upper()
    if res == 'N':
        break
print(f'quantidade de pessoas com mais de 18 anos: {maiores}')
print(f'quantidade de homens: {homens}')
print(f'quantidade de mulheres com menos de 20 anos: {mulheresNovas}')