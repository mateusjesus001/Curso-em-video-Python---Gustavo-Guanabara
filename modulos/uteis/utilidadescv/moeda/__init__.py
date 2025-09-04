def aumentar(x,y,f=False):
    if ',' in x:
      f = False
      x = x.split(',')
      lista = []
      lista.append(x[0])
      lista.append('.')
      lista.append(x[1])
      msg = ''
      for h in lista:
       msg += h
      msg = float(msg)
      msg = msg + ((y/100)*msg)
      return f'R${msg}'
    else:
     x = float(x)
     s = x + ((y/100)*x)
     if f == True:
      return f'R${s:.0f},00'
     return s


def diminuir(x,y,f=False):
    if ',' in x:
      f = False
      x = x.split(',')
      lista = []
      lista.append(x[0])
      lista.append('.')
      lista.append(x[1])
      msg = ''
      for h in lista:
       msg += h
      msg = float(msg)
      msg = msg - ((y/100)*msg)
      return f'R${msg}'
    else:
     x = float(x)
     s = x - ((y/100)*x)
     if f == True:
      return f'R${s:.0f},00'
     return s


def metade(x,f=False):
     if ',' in x:
      f = False
      x = x.split(',')
      lista = []
      lista.append(x[0])
      lista.append('.')
      lista.append(x[1])
      msg = ''
      for h in lista:
       msg += h
      msg = float(msg)
      msg = msg/2
      return f'R${msg}'
     else:
      x = float(x)
      s = x/2
      if f == True:
       return f'R${s:.0f},00'
      return s

def dobro(x,f=False):
    if ',' in x:
      f = False
      x = x.split(',')
      lista = []
      lista.append(x[0])
      lista.append('.')
      lista.append(x[1])
      msg = ''
      for h in lista:
       msg += h
      msg = float(msg)
      msg = msg*2
      return f'R${msg}'
    else:
     x = float(x)
     s = x*2
     if f == True:
      return f'R${s:.0f},00'
     return s


def moeda(txt):
 if ',' in txt:
   return f'R${txt}'
 else:
  txt = float(txt)
  return f'R${txt:.0f},00'

def resumo(a,b=0,c=0):
 print('-'*30)
 print('RESUMO DO VALOR'.center(30))
 print('-'*30)
 print(f'Preço analisado: ', end = '')
 x = moeda(a)
 print(f'{x.center(12)}')
 print(f'Dobro do preço: ', end = '')
 if ',' in a:
  strparam = a.split(',')
  msgx = ''
  listafinal = []
  listafinal.append(strparam[0])
  listafinal.append('.')
  listafinal.append(strparam[1])
  for x in listafinal:
   msgx += x
  msgx = float(msgx)
 else:
   msgx = float(a)
 d = msgx
 if d*2 >= 1000:
  d = dobro(a,True)
  print(f'{d.center(15)}')
 else:
  d = dobro(a,True)
  print(f'{d.center(14)}')
 m = metade(a,True)
 print(f'Metade do preço: ', end = '')
 print(f'{m.center(12)}')
 au = (msgx + ((b/100)*msgx))
 au = str(au)
 aumento = moeda(au)
 print(f'{b}% de aumento: ', end = '')
 print(f'{aumento.center(14)}')
 red = (msgx - ((c/100)*msgx))
 red = str(red)
 redução = moeda(red)
 print(f'{c}% de redução: ', end = '')
 print(f'{redução.center(14)}')
 print('-'*30)

