list = [[],[],[]]
cont = 0
for c in range(0,9):
 while cont < 3:
  num = int(input('Digite um número: '))
  list[0].append(num)
  cont += 1
 while cont < 6:
  num = int(input('Digite um número: '))
  list[1].append(num)
  cont += 1
 while cont < 9:
  num = int(input('Digite um número: '))
  list[2].append(num)
  cont += 1
for c in list[0]:
 print(f'[ {c} ]', end = '')
print()
for c in list[1]:
 print(f'[ {c} ]', end = '')
print()
for c in list[2]:
 print(f'[ {c} ]', end = '')
