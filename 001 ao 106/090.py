dict = {}
dict['nome'] = str(input('Digite seu nome: '))
dict['media'] = float(input('Digite sua média: '))
print(f'Nome é igual a {dict["nome"]}')
print(f'Média é igual a {dict["media"]}')
if dict["media"] >= 7:
 print('Situação é igual aprovado')
elif dict["media"] >= 5 and dict["media"] < 7:
 print('Situação é igual a recuperação')
else:
 print('Situação é igual reprovado')


