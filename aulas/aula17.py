# num = [2, 6, 3, 9]
# num.append(7)
# num.sort() #ordena o array
# num.sort(reverse=True) #coloca do maior para o menor
# num.insert(2, 0) #primeiro indica a posiçao e depois insere o valor nela
# num.pop() #remove o ultimo, se quiser remover um especifico basta por entre os ()

# if 4 in num:
#     num.remove(4)
# else:
#     print('nao achei o numero 4')

# print(num)
# print(f'essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for cont in range(0, 4):
    num = int(input('Digite um valor: '))
    valores.append(num)
    cont += 1

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}')
print('FIM')

a = [1, 7, 4, 8]
# b = a #isso faz uma ligação apenas
b = a[:] #isso faz uma cópia da lista
b[2] = 8