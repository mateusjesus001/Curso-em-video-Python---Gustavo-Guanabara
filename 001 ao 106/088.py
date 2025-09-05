from random import randint as rand
from time import sleep as givemeasecond
list = []
cont = 1
cont2 = 0
print('-'*30)
print('JOGA NA MEGA SENA'.center(30))
print('-'*30)
jogos = int(input('Quantos jogos vc quer que eu sorteie ? '))
print(f'-=-=-=SORTEANDO {jogos} JOGOS=-=-=-')
while cont < jogos+1:
 print(f'\nJogo{cont}', end = '')
 while cont2 < 6:
  n = rand(1,60)
  if n not in list:
   list.append(n)
   cont2 +=1
 print(f'{sorted(list)}', end = '')
 list.clear()
 givemeasecond(0.5)
 cont += 1
 cont2 = 0
print()
print('-=-=-=<BOA SORTE!>=-=-=-'.center(25))
 