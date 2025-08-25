tabela_campeonato = (
    "Flamengo",
    "Palmeiras",
    "Cruzeiro",
    "Bahia",
    "Botafogo",
    "Mirassol",
    "São Paulo",
    "Fluminense",
    "RB Bragantino",
    "Ceará",
    "Atlético-MG",
    "Internacional",
    "Grêmio",
    "Corinthians",
    "Santos",
    "Vasco",
    "Vitória",
    "Juventude",
    "Fortaleza",
    "Sport"
)

print(f''' 5 melhores colocados no brasileirão 2025:
{tabela_campeonato[0:5]}
''')
print(f'''Clubes na zona de rebaixamento: 
{tabela_campeonato[-4:]}
''')

print(f'A tabela em ordem alfabética')
for c in sorted(tabela_campeonato):
    print(c)

print(f'O Santos está na posição: {tabela_campeonato.index("Santos")+1}')