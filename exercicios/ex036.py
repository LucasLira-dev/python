casaValor = float(input('Digite o valor da casa: '))

salario = float(input('Digite seu salário: '))

anos = int(input('Em quantos anos voce irá pagar? '))

prestacao = casaValor / (anos * 12)

porcentagem = (salario * 0.3) / 100

if prestacao > porcentagem:
    print('Emprestimo negado')
elif prestacao < porcentagem:
    print('Seu emprestimo foi aprovado')