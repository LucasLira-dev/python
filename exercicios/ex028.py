import random 

numSort = random.randint(0, 5) # sorteia um número entre 0 e 5

num = int(input('Tente adivinhar o número que eu pensei (entre 0 e 5): '))

if num == numSort:
    print(f'Parabéns! Você acertou, o número era {numSort}.')
else:
    print(f'Você errou! O número que eu pensei era {numSort}.')