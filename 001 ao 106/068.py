from random import randint
print('-=-=-=Par-Ou-Ímpar=-=-=-')
comp = jog = par = impar = venc = 0
while True:
 jog = int(input('digite um número de 1 a 10: '))
 if jog <= 10:
  result = str(input('Vc quer par ou ímpar ? [P/I] ')).upper()[0]
  comp = randint(1,10)
  print(f'o computador escolheu {comp}')
  if result == 'P':
   if (jog+comp) % 2 == 0:
    print(f'Vc jogou {jog} e o computador jogou {comp}, {jog+comp} é par, Vc Venceu')
    venc += 1
   else:
    print(f'Vc jogou {jog} e o computador jogou {comp}, {jog+comp} é ímpar, Vc Perdeu')
    break
  if result == 'I':
   if (jog+comp) % 2 != 0:
    print(f'Vc jogou {jog} e o computador jogou {comp}, {jog+comp} é ímpar, Vc Venceu')
    venc += 1
   else:
    print(f'Vc jogou {jog} e o computador jogou {comp}, {jog+comp} é par, Vc Perdeu')
    break
 else:
  print('Número inválido, digite um número de 1 a 10')
  
print(f'Vc venceu {venc} tentativas')