def leiaint(txt):
 try:
  while True:
   n = input(txt)
   if n not in ' abcdefghijklmnopqrstuvwxyz.,;~':
    cont = 0
    for c in n:
     if c in ' abcdefghijklmnopqrstuvxwyz.,;~':
      cont += 1
    if cont == 0:
     return n
    else:
     print(f'\033[1;31mErro digite um número inteiro válido !\033[m')
   else:
    print(f'\033[1;31mErro digite um número inteiro válido !\033[m')
 except KeyboardInterrupt:
  print(f'\n\033[1;31mO usuário preferiu não digitar esse número.\033[m')
  n = 0
  return n



def leiafloat(txt2):
 try:
  while True:
   f = input(txt2).replace(',','.')
   if f not in ' abcdefghijklmnopqrstuvwxyz,;~':
    cont = 0
    for d in f:
     if d in ' abcdefghijklmnopqrstuvwxyz,;~':
      cont += 1
    if cont == 0:
     return f
    else:
     print(f'\033[1;31mErro digite um número real válido !\033[m')
   else:
     print(f'\033[1;31mErro digite um número real válido !\033[m')
 except KeyboardInterrupt:
   print(f'\n\033[1;31mO usuário preferiu não digitar esse número.\033[m')
   f = 0
   return f
  
n = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um número real: ')
print(f'Vc digitou o numero inteiro {n} e o número real {f}')
  


   

   
   
 