# pessoas = {
#     'nome': 'Lucas',
#     'sexo': 'M',
#     'idade': 21
# }

# pessoas['peso'] = 76 #adiciona um novo elemento
# # del pessoas['sexo'] #deleta chave e valor

# # print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')

# # print(pessoas.keys()) #mostra as chaves(nome, sexo e idade)
# # print(pessoas.values()) #mostra os valores

# for k, v in pessoas.items():
#     print(f'{k} = {v}')


# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'Ceará', 'sigla': 'CE'}
# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil)

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) #copia o conteudo

for c in brasil:
    for k, v in c.items():
        print(f'O campo {k} tem valor {v}')