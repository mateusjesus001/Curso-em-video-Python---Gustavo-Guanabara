from random import randint
from time import sleep
itens = ['pedra','papel','tesoura']
computador = randint(0,2)
print(''' Escolha uma opção
[0] Pedra
[1] Papel 
[2] Tesoura''')
jogador = int(input('Escolha uma opção: '))
if jogador == 0 or jogador == 1 or jogador == 2:
  print('JO')
  sleep(1)
  print('KEN')
  sleep(1)
  print('PO!!!')
  print('-='*12)
  print(f'O computador escolheu {itens[computador]}')
  print(f'O jogador escolheu {itens[jogador]}')
  print('-='*12)
  if jogador == 0: #jogador escolheu pedra
   if computador == 0:
    print('Empate')
 
   elif computador == 1:
    print('Computador venceu')
   elif computador == 2:
    print('Jogador venceu')
  elif jogador == 1: #jogador escolheu papel
   if computador == 0:
    print('Jogador venceu')
 
   elif computador == 1:
    print('Empate')
   elif computador == 2:
    print('Computador venceu')
  elif jogador == 2: #jogador escolheu teoura
   if computador == 0:
    print('Computador venceu ')
   elif computador == 1:
    print('Jogador venceu')
 
   elif computador == 2:
    print('Empate')
else: #jogador digitou um número fora de 0,1,2
 print('jogada inválida')

