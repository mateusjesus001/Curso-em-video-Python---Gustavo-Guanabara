list = []
pessoas = 0
mediaidade = 0
mulheres = []
mulher = 'F'
acimamedia = 0
cont3 = -1
while True:
 nome = input('Digite seu nome: ')
 sexo = input('Digite seu sexo: ').strip().upper()[0]
 while sexo not in 'MmFf':
  sexo = input('Sexo inválido, digite F ou M: ').strip().upper()[0]
 idade = int(input('Digite sua idade: '))
 pessoas += 1
 dict = {}
 dict['nome'] = nome
 dict['sexo'] = sexo
 dict['idade'] = idade
 list.append(dict.copy())
 del(dict)
 resposta = input('Deseja continuar ? [S/N] ')
 while resposta not in 'SsNn':
  resposta = input('Resposta inválida, digite [S/N] ')
 if resposta in 'Nn':
  break
for c in range(len(list)):
  mediaidade += list[c]['idade']
mediaidade = mediaidade/pessoas
print(list)
for i in list:
 cont3 +=1
 for v in i.values():
  if v == mulher:
   mulheres.append(list[cont3]['nome'])
for c in range(len(list)):
 if list[c]['idade'] > mediaidade:
  acimamedia += 1
print(f'Foram cadastradas {pessoas} pessoas')
print(f'A média de idade do grupo é {mediaidade:.2f}')
print(f'As mulheres cadastradas são: ', end = '')
for mulher in mulheres:
 print(f'{mulher} ', end = '')
print()
print(f'Existem {acimamedia} pessoas acima da média no cadastro')
for c in range(len(list)):
 if list[c]['idade'] > mediaidade:
  for k,v in list[c].items():
   print(f'{k} = {v} ', end = '')
  print()
  

 
