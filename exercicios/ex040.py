n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a primeira nota: '))

media = (n1 + n2 ) / 2

if media < 5.0:
    input(f'Sua média foi: {media}! voce está REPROVADO!!!!!!')
elif media > 5.0 and media < 7.0:
    input(f'Sua média foi: {media}! voce está de RECUPERAÇÃO!!!!!!')
elif media >= 7.0:
    input(f'Sua média foi: {media}! voce foi APROVADO!!!!!')