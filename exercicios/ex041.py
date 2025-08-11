ano = int(input('Digite em que ano voce nasceu: '))

idade = 2025 - ano

if idade <= 9:
    print('Voce está na categoria MIRIM!')
elif idade <= 14:
    print('Voce está na categoria INFANTIL!')
elif idade <= 19:
    print('Voce está na categoria JUNIOR!')
elif idade <= 20:
    print('Voce está na categoria SENIOR')
else:
    print('Voce está na categoria MASTER!')