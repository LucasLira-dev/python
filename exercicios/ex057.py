sexo = input('''
Informe seu sexo:
[F] - Feminino
[M] - Masculino ''').upper()

while sexo != "F" and sexo != "M":
    sexo = input('''
    Escolha uma opção válida: 
    [F] - Feminino
    [M] - Masculino ''').upper()
print('Olá')