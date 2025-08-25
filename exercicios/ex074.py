import random

nums = []
maior = 0
menor = 0

for c in range(0, 5):
    nums.append(random.randint(1,10))
tupla = (nums)
print(tupla)

print(f'O maior número foi: {max(tupla)}')
print(f'O menor número foi: {min(tupla)}')
    
