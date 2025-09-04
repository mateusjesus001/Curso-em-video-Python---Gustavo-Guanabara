while True:
 tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','desesseis','desessete','dezoito','desenove','vinte')
 n= int(input('digite um número de 0 a 20: '))
 if n >= 0 and n <= 20:
  print(f'Vc digitou o número {tupla[n]}')
 else:
  print('Vc digitou um número invlálido, digite um número de 0 a 20')
 r = input('Quer continuar ? [S/N]  ').strip().upper()[0]
 if r == 'N':
  break