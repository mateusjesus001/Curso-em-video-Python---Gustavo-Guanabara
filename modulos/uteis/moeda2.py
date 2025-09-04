def aumentar(x,y,f=False):
    s = x + ((y/100)*x)
    if f == True:
     return f'R${s:.0f},00'
    return s


def diminuir(x,y,f=False):
    s = x - ((y/100)*x)
    if f == True:
     return f'R${s:.0f},00'
    return s


def metade(x,f=False):
     s = x/2
     if f == True:
      return f'R${s:.0f},00'
     return s

def dobro(x,f=False):
    s = x*2
    if f == True:
     return f'R${s:.0f},00'
    return s


def moeda(txt):
 return f'R${txt:.0f},00'

def resumo(a,b=0,c=0):
 print('-'*30)
 print('RESUMO DO VALOR'.center(30))
 print('-'*30)
 print(f'Preço analisado: ', end = '')
 x = moeda(a)
 print(f'{x.center(12)}')
 print(f'Dobro do preço: ', end = '')
 d = a
 if d*2 >= 1000:
  d = dobro(a,True)
  print(f'{d.center(15)}')
 else:
  d = dobro(a,True)
  print(f'{d.center(14)}')
 m = metade(a,True)
 print(f'Metade do preço: ', end = '')
 print(f'{m.center(12)}')
 aumento = moeda(a + ((b/100)*a))
 print(f'{b}% de aumento: ', end = '')
 print(f'{aumento.center(14)}')
 redução = moeda(a - ((c/100)*a))
 print(f'{c}% de redução: ', end = '')
 print(f'{redução.center(14)}')
 print('-'*30)

