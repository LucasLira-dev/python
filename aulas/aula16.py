#tuplas
lanche = ('Hamburguer', 'pudim', 'bolo', 'suco')

# for comida in lanche:
#     print(f'eu vou comer {comida}')


# for c in range(0, len(lanche)):
#     print(lanche[c])


for pos, comida in enumerate(lanche):
    print(f'vou comer {comida} na posição {pos}')

# #mostra ordem alfabetica
# print(sorted(lanche))

# #fatiamento
# print(lanche[2:3])

#pegando o index de um lanche especifico
print(lanche.index("bolo"))