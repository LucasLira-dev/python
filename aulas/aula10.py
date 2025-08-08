n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m >= 6:
    print(f'A média é {m:.1f}, você foi aprovado!')
else:
    print(f'Média: {m:.1f} Você é muito burro e foi reprovado!')