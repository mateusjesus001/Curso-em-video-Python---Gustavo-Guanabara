listpareninicial = []
listparenfinal = []
exp = str(input('digite uma expressão: ')).strip()
for item in exp:
    if item == '(':
     listpareninicial.append(item)
    if item == ')':
     listparenfinal.append(item)
if len(listpareninicial) == len(listparenfinal):
  print('Essa expressão é válida')
else:
  print('Essa expressão não é válida')
       

