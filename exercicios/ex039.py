ano = int(input('Digite o ano em que voce nasceu: '))

idade = 2025 - ano

if idade == 18:
    print('Voce precisa se alistar')
elif idade < 18:
    print(f'Voce ainda não tem idade para se alistar. ainda faltam {18-idade} anos para voce.')
else:
    print(f'Voce ja passou {idade - 18} anos da idade para se alistar')