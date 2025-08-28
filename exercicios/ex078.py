valores = []

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if menor > valores[c]:
            menor = valores[c]

posicoes_maior = []
posicoes_menor = []

for indice, valor in enumerate(valores):
    if valor == maior:
        posicoes_maior.append(indice)
    if valor == menor:
        posicoes_menor.append(indice)

# posicoes_maior = [i for i, v in enumerate(valores) if v == maior]
# posicoes_menor = [i for i, v in enumerate(valores) if v == menor]

print(f'O maior valor na lista é: {maior} nas posições: {posicoes_maior}')
print(f'O menor valor na lista é: {menor} nas posições: {posicoes_menor}')