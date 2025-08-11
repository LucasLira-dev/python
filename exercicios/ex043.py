peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura*altura)

if imc < 18.5:
    print(f'seu IMC é: {imc:.2f}! voce está abaixo do peso!')
elif imc < 25:
    print(f'seu IMC é: {imc:.2f}! voce está no peso ideal!')
elif imc < 30:
    print(f'seu IMC é: {imc:.2f}! voce está com sobrepeso!')
elif imc < 40:
    print(f'seu IMC é: {imc:.2f}! voce está OBESO!')
else:
    print(f'seu IMC é: {imc:.2f}! ALERTA! voce está com obesidade mórbida')