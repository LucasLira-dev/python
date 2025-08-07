import random

aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')

print(f'o aluno escolhido foi: {random.choice([aluno1, aluno2, aluno3, aluno4])}')