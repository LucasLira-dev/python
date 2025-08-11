preco = float(input('Digite o preço do produto: '))

pagamento = float(input('''
Digite 1 para pagar á vista com dinheiro/cheque
Digite 2 para pagar á vista com o cartão
Digite 3 para pagar em até 2x no cartão
Digite 4 para pagar em 3x ou mais no cartão
'''))

if pagamento == 1:
    print(f'Voce terá que pagar: {preco - (preco*0.10)} reais')
elif pagamento == 2:
    print(f'Voce terá que pagar: {preco - (preco*0.05)} reais')
elif pagamento == 3:
    print(f'Voce terá que pagar: {preco} reais')
elif pagamento == 4:
    print(f'Voce terá que pagar: {preco + (preco*0.20)} reais')
else:
    print('Digite uma opção válida')