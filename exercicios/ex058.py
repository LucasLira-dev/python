import random 

numSort = random.randint(1, 10)

print('-----TENTE-ME-VENCER-----')
humano = int(input('Digite um número entre 1 e 10: '))
tentativas = 1

if humano <= 10:
    while humano != numSort:
        tentativas += 1
        print(f'''Voce errou :(
        eu escolhi {numSort} HAHAHHAHHAHAHHAHAH''')
        humano = int(input(f'''
        ---{tentativas}ª TENTATIVA---
        Digite um número: '''))
        numSort = random.randint(1, 10)
    if tentativas < 5:
        print('AEEEEEEEEEEEEE VOCE ACERTOU (e em menos de 5 tentativas, uma verdadeira MÁQUINA)')
    elif tentativas < 10:
        print('''
        AEEEEE VOCE ACERTOU! 
        Já tava na hora né?''')
    else:
        print('''UHUL! O IMPOSSIVEL ACONTECEU MEU DEUS DO CÉU, VOCE ACERTOU!!!!
        (depois de uma década tentando)''')
else:
    print(' VOCE NÃO SABE LER???? é de 1 até 10 cara...')