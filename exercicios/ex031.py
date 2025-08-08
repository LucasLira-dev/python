distancia = float(input('Digite a distância em km: '))

if distancia <= 200:
    print(f' voce terá que pagar: {distancia * 0.50} R$')
else:
    print(f' voce terá que pagar: {distancia * 0.45} R$')