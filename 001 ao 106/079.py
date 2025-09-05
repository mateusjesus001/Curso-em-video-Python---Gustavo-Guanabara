list = []
while True:
 n = int(input('digite um valor: '))
 if n not in list:
  list.append(n)
 else:
  print('Vc digitou um valor que já existe na lista')
 r = input('Deseja continuar ? [S/N]  ').strip().upper()[0]
 while r not in 'SN':
  r = input('Deseja continuar ? [S/N]  ').strip().upper()[0]
 if r == 'N':
  break
print(sorted(list))
