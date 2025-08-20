import random

print('---------------------')
print('Vamos jogar Par ou Impar!')

vitorias = 1

while True:
    numeroHumano = int(input('Digite um número: '))
    numeroComputador = random.randint(0, 100)
    escolha = input('PAR ou IMPAR? [P/I]').strip().upper()
    soma = numeroHumano + numeroComputador

    if soma % 2 == 0:
        resultado = 'PAR'
    elif soma % 2 == 1:
        resultado = 'IMPAR'
    
    if (resultado == 'PAR' and escolha != 'P') or (resultado == 'IMPAR' and escolha != 'I'):
        break

    print(f'''VOCE VENCEUUUUU! eu escolhi {numeroComputador} e voce {numeroHumano}....  {soma} é {resultado}
    vitorias seguidas: {vitorias}''')
    print('---------------------')
    print('Vamos jogar dnv!')
    vitorias += 1
    
print(f'VOCE PERDEU... voce escolheu {numeroHumano} e eu {numeroComputador}... o total é {soma} que é {resultado}!')