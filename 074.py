from random import randint
tupla = ''
maior = menor = cont = 0
for c in range(0,4):
 sort = str(randint(0,9))
 tupla += sort
 if c == 0:
  maior = menor = sort
 else:
  if sort > maior:
   maior = sort
  if sort < menor:
   menor = sort
print(f'Os valores sorteados foram ', end = '')
for item in tupla:
 cont += 1
 if cont < 4:
  print(f'{item}  ', end = '')
else:
 print(item)
print(f'O maior valor na tupla foi {maior} e o menor foi {menor}')
