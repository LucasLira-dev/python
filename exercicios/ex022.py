nome = input(' Digite seu nome completo: ')

print(f'''o seu nome em maisculo  é {nome.upper()}
o seu nome em minusculo é {nome.lower()}
o seu nome tem {len(nome) - nome.count(' ')} letras
o seu primeiro nome tem {len(nome.split()[0])} letras''')


# o COUNT conta quantos elementos especificados tem na string
# o SPLIT divide a string em uma lista de palavras
# o LOWER transforma a string em minusculo
# o UPPER transforma a string em maisculo
# o LEN conta quantos caracteres tem na string
# o CAPITALIZE transforma a primeira letra da string em maisculo
# o TITLE transforma a primeira letra de cada palavra em maisculo
# o STRIP remove os espaços no começo e no final da string
# o REPLACE substitui uma parte da string por outra
# o FIND procura uma parte da string e retorna a posição
# o STLIP junta as palavras da string em uma só
# o JOIN junta as palavras da lista em uma string