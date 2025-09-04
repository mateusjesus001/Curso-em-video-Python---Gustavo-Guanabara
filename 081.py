cont = 0
list = []
while True:
 list.append(int(input('Digite um valor: ')))
 cont += 1
 r = input('quer continuar ? [S/N] ').strip().upper()[0]
 while r not in 'SN':
  r = input('quer continuar ? [S/N] ').strip().upper()[0]
 if r == 'N':
  break
print(f'Vc digitou {cont} valores')
print(list[-1::-1])
if 5 in list:
 print(f'O valor 5 foi digitado e está na posição {list.index(5)}')
else:
 print('O valor 5 não está na lista')
 