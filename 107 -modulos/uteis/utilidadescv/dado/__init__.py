def leiadinheiro(msg):
 while True:
  k = input(msg)
  if k != '':
   if k[0] in '0123456789-1-2-3-4-5-6-7-8-9':
    cont = 0
    for n in k:
     if n in ' abcdefghijklmnopqrstuvwxyz':
      cont += 1
    if cont != 0:
     print(f'\033[1;31;40mValor inválido\033[m')
    else:
     return k
   else:
    print(f'\033[1;31;40mValor inválido\033[m')

  else:
   print(f'\033[1;31;40mValor inválido\033[m')

 




