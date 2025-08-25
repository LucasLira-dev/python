produtos = (
    'Pão', 2.50,
    'Leite', 4.80,
    'Café', 9.90,
    'Arroz', 23.50,
    'Feijão', 8.75,
    'Óleo', 6.40,
    'Açúcar', 3.20,
    'Macarrão', 5.00,
    'Farinha', 4.50,
    'Biscoito', 2.90
)

#pula de 2 em 2
for i in range(0, len(produtos), 2):
   print(f'{produtos[i]}: R$ {produtos[i+1]}')