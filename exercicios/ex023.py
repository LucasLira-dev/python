num = int(input('Digite um número entre 0 e 9999: '))

print(f''' Analisando o número {num}:
Unidade: {num % 10}
Dezena: {num // 10 % 10}
Centena: {num // 100 % 10}
Milhar: {num // 1000 % 10}
''') 

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
# o JOIN junta as palavras da lista em uma string
# o IN verifica se um elemento está presente na string
# o rfind procura uma parte da string e retorna a posição da ultima aparição
# o rstrip remove os espaços no final da string
# o lstrip remove os espaços no começo da string
