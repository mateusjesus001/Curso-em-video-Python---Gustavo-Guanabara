def leiaint(txt):
 while True:
  cond1 = 0
  cont1 = 0
  pergunta = input(txt)
  if pergunta != '':
   primeiroitem = pergunta[0]
   for c in pergunta:
    if c in ' abcdefghijklmnopqrstuvwxzy,.':
     cont1 += 1
   if cont1 >= 1:
    print(f'\033[1;31;40mErro digite um número inteiro !\033[;;m')
    cond1 = 1
   if primeiroitem in '0123456789-1-2-3-4-5-6-7-8-9' and cond1 == 0:
    return pergunta
  else:
   print(f'\033[1;31;40mErro digite um número inteiro !\033[;;m')
n = leiaint('Digite um número: ')
print(f'Vc acabou de digitar o número {n}')


  