nome = input(' Digite seu nome completo: ').strip() #remove espaços no começo e no final

print(f'''o seu primeiro nome é {nome.split()[0]}
o seu último nome é {nome.split()[-1]}''')