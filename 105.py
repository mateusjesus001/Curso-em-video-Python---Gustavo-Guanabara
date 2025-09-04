def notas(*num, sit=False):
 dict = {}
 cont = 0
 maior = menor = media = soma = 0
 for c in num:
  soma += c
  if cont == 0:
   maior = menor = c
  else:
   if c > maior:
    maior = c
   if c < menor:
    menor = c
  dict[f'Aluno {cont+1}'] = c
  cont += 1
 media = soma/cont
 dict['Maior nota'] = maior
 dict['Menor nota'] = menor
 dict['Média da turma'] = media
 if sit == True:
  if media < 5:
   dict['Situação'] = 'Ruim'
  elif media >=5 and media < 7:
   dict['Situaçao'] = 'Regular'
  elif media >= 7:
   dict['Situação'] = 'Boa'
 
 return dict


print(notas(10,10,10,10, sit = True))
