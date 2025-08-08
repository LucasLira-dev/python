salario = float(input('Digite seu salário: '))

if salario >= 1250:
    print(f'seu novo salario será: {salario + (salario * 0.10)}')
else:
    print(f'seu novo salario será: {salario + (salario * 0.15)}')