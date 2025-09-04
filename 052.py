n = int(input('digite um número:  '))
v = 0
f = 0
if n ==2:
  print(f'{n} é primo')
elif n ==3:
  print(f'{n} é primo')
elif n ==1:
 print(f'{n} não é primo')
elif n%2 ==0:
  print(f'{n} não é primo')
else:
   if n%3 ==0 or n%4 == 0 or n%5 ==0 or n%6 == 0 or n%7 == 0 or n%8 == 0 or n%9 ==0:
    f=1
   else:
    v = 1
if v!= 0:
  print(f'{n} é primo')    
if f!= 0:
  print(f'{n} não é primo')