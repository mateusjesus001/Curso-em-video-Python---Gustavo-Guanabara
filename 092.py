dict = {}
anoatual = 2023
nome = input('digite seu nome: ')
anodenascimento = int(input('Digite o ano do seu nascimento: '))
carteira = int(input('Digite sua carteira de trabalho: '))
idade = anoatual - anodenascimento
if carteira != 0:
 anocontrato = int(input('Digite o ano de contratação: '))
 salario = float(input('Digite seu salário: '))
 contribuicao = 30
 aposento = anocontrato + contribuicao - anodenascimento
 dict['nome'] = nome
 dict['idade'] = idade
 dict['ctps'] = carteira
 dict['contratação'] = anocontrato
 dict['salário'] = salario
 dict['aposentadoria'] = aposento
 print(dict)
 for k,v in dict.items():
  print(f'{k} tem o valor {v}')
else:
 dict['nome'] = nome
 dict['idade'] = idade
 dict['ctps'] = carteira
 print(dict)
 for k,v in dict.items():
  print(f'{k} tem o valor {v}')
