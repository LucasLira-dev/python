totalPagar = menorPreco = maisCaros = 0
nomeMaisBarato = ''

while True: 
    print('-------------------')
    print('Carrinho de compras')
    nome = input('Digite o nome do produto: ')
    preco = int(input('Digite o preço do produto: '))
    if totalPagar == 0:
        menorPreco = preco
        nomeMaisBarato = nome
    if preco < menorPreco:
        menorPreco = preco
        nomeMaisBarato = nome
    totalPagar += preco
    if preco > 1000:
        maisCaros += 1
    print('-------------------')
    res = input('Quer continuar? [S/N] ').upper()
    if res == 'N':
        break
print(f'O custo total dos produtos é: {totalPagar}')
print(f'total de produtos que custam mais de 1000 R$: {maisCaros}')
print(f'O produto mais barato é: {nomeMaisBarato}')