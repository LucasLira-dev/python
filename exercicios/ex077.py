palavras = (
    'python',
    'programa',
    'desafio',
    'computador',
    'algoritmo',
    'tupla',
    'lista',
    'função',
    'variável',
    'condição'
)

vogais = (
    'a',
    'e',
    'i', 
    'o',
    'u'
)

vogaisEncontradas = []

for palavra in palavras:
    vogaisEncontradas = []
    for vogal in vogais:
        if vogal in palavra:
            vogaisEncontradas.append(vogal)
    print(f'a palavra {palavra} tem as vogais: {vogaisEncontradas}')