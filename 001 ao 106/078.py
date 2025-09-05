list = []
maior = menor = cont = 0
for c in range(0,5):
  list.append(int(input('Digite um número: ')))
for item in list:
  if cont == 0:
   maior = menor = item
  else:
    if item > maior:
      maior = item
    if item < menor:
      menor = item
  cont += 1
print(f'O maior valor foi {maior} nas posições ', end = '')
for i,v in enumerate(list):
  if v == maior:
   print(f'{i}... ', end = '')
print(f'\nO menor valor foi {menor} nas posições ', end = '')
for i,v in enumerate(list):
  if v == menor:
    print(f'{i}... ', end = '')


