def interactivehelp():
 from time import sleep
 txt1 = 'SISTEMA DE JUDA PYHELP'
 txt2 = 'Acessando o local do comando'
 tam1 = len(txt1)+4
 tam2 = len(txt2)+4
 tam3 = 12
 while True:
  sleep(2)
  print(f'\033[1;30;42m')
  print('~'*tam1)
  print(f'  {txt1}')
  print('~'*tam1)
  print(f'\033[1;30;40m')
  escolha = input('Função ou biblioteca ')
  if escolha == '':
   print(f'\033[1;30;41m')
   print('~'*tam3)
   print('Até Logo!'.center(tam3))
   print('~'*tam3)
   break
  if escolha[0] in 'Ff':
   print(f'\033[1;30;41m')
   print('~'*tam3)
   print('Até Logo!'.center(tam3))
   print('~'*tam3)
   break
  print(f'\033[1;30;44m')
  print('~'*(tam2+len(escolha)))
  print(f'  {txt2} ', end = '')
  print(escolha)
  print('~'*(tam2+len(escolha)))
  print(f'\033[1;30;47m')
  print(f'{help(escolha)}')

interactivehelp()
