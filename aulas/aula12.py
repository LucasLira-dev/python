nome = input('Digite seu nome: ').capitalize()

if nome == 'Lucas':
    print('Olá Lucas, tudo bem?')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Ana':
    print(f'Olá {nome}, seu nome é bem popular!')
elif nome in 'Ana mariana julia':
    print('Belo nome feminino')
else:
    print('oi')
print(f'Tenha um bom dia {nome}')