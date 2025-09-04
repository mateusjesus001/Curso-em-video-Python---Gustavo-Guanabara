list = [[],[],[]]
linha1 = 0
linha2 = 1
linha3 = 2
cont = cont2 = pares = terceiracoluna = maior = 0
for c in range(0,9):
 while cont2 < 3:
  num = int(input(f'Digite o número {linha1}{linha1+cont} '))
  list[0].append(num)
  if num %2 == 0:
   pares += num
  if list[0].index(num) == 2:
   terceiracoluna += num
  cont +=1
  cont2 +=1
 cont = 0
 while cont2 < 6:
  num = int(input(f'Digite o número {linha2}{linha1+cont} '))
  list[1].append(num)
  if num %2 == 0:
   pares += num
  if list[1].index(num) == 2:
   terceiracoluna += num
  if list[1].index(num) == 0:
   maior = num
  else:
   if num > maior:
    maior = num
  cont +=1
  cont2 +=1
 cont = 0
 while cont2 < 9:
  num = int(input(f'Digite o número {linha3}{linha1+cont} '))
  list[2].append(num)
  if num %2 == 0:
   pares += num
  if list[2].index(num) == 2:
   terceiracoluna += num
  cont += 1
  cont2 += 1
for c in list[0]:
 print(f'[ {c} ]', end = '')
print()
for c in list[1]:
 print(f'[ {c} ]', end = '')
print()
for c in list[2]:
 print(f'[ {c} ]', end = '')
print()
print('-='*30)
print(f'A soma dos pares foi {pares}')
print(f'A soma dos valores da terceira coluna foi {terceiracoluna}')
print(f'O maior valor da segunda linha foi {maior}')





 

  
