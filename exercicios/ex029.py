velocidade = int(input('Qual a velocidade do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado! O valor da multa é R$ {multa:.2f}.')
else:
    print('Você está dentro do limite de velocidade. Boa viagem!')