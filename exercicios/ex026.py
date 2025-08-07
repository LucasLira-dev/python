frase = input('Digite uma frase: ')

print(f'''A letra "A" aparece {frase.upper().count("A")} vezes na frase.
      a primeira aparição da letra "A" é na posição {frase.upper().find("A")}
a ultima aparição da letra "A" é na posição {frase.upper().rfind("A")}''')