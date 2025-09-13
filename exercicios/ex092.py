from datetime import date

dados = {}
ano_atual = date.today().year

dados['nome'] = str(input('Digite o nome: '))
ano = int(input('Ano de nascimento: '))
idade = ano_atual - ano
dados['idade'] = idade
dados['cpts'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['cpts'] != 0:
    dados['contratacao'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    aposentadoria = 35 - (ano_atual - dados['contratacao']) + dados['idade']
    dados['aposentadoria'] = aposentadoria

for k, v in dados.items():
    print(f'{k}: = {v}' )