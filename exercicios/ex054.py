
maiores = 0
menores = 0

for c in range(0, 7):
    ano = int(input('Digite o ano do seu nascimento: '))
    if 2025 - ano >= 18:
        maiores += 1
    else:
        menores += 1
print(f'a quantidade de pessoas maiores de idade: {maiores}')
print(f'a quantidade de pessoas menores de idade: {menores}')
