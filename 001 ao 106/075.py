tupla = ''
for c in range(0,4):
 num = int(input('digite um número: '))
 tupla += str(num)
if '9' in tupla:
 print(tupla.count('9'))
if '3' in tupla:
 print(tupla.index('3'))
for item in tupla:
 item = int(item)
 if item %2 == 0:
  print(f'{item} ', end = '')