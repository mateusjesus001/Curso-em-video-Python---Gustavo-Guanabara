cond = 0
while cond ==0:
 print('-=-=Menu=-=-')
 num1 = float(input('digite o primeiro número:  '))
 num2 = float(input('digite o segundo número:  '))
 print('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa')
 opção = int(input('Escolha uma opção: '))
 if opção == 1:
  print(f'{num1+num2:.0f}')
 if opção == 2:
  print(f'{num1*num2:.0f}')
 if opção == 3:
  if num1 > num2:
   print(num1)
  elif num1 < num2:
   print(num2)
  else:
   print('Eles são iguais')
 if opção == 4:
  cond = 0
 if opção == 5:
  cond = 1
print('Programa Finalizado')