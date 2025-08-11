num = int(input('Digite um número: '))

tipo = int(input('Escolha o tipo de conversão para o número:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n'))

if tipo == 1:
    print(f'O número {num} em binário é {bin(num)[2:]}')
elif tipo == 2:
    print(f'O número {num} em octal é {oct(num)[2:]}')
elif tipo == 3:
    print(f'O número {num} em hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida!')