list = []
while True:
 list.append(int(input('digite um número: ')))
 r = input('Quer continuar ? [S/N] ').strip().upper()[0]
 while r not in 'SN':
  r = input('Quer continuar ? [S/N] ').strip().upper()[0]
 if r == 'N':
  break
 listpar = []
 listimpar = []
for item in list:
  if item %2 == 0:
   listpar.append(item)
  else:
   listimpar.append(item)
print(f'{list}\n{listpar}\n{listimpar}')
  
