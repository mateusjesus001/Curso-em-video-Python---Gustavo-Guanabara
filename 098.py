def contador(inicio,fim,passo):
    for c in range(1,11):
     print(f'{c}',end = '')
    print()
    for c in range(10,0,-2):
     print(f'{c}',end = '')
    print()
    if inicio > fim:
     if passo > 0:
       passo = passo*-1
     if passo == 0:
       passo = -1
     print(f'Contagem de {inicio} a {fim+1} indo de {passo*-1} em {passo*-1}')
    if inicio < fim:
     if passo < 0:
       passo = passo*-1
     print(f'Contagem de {inicio} a {fim-1} indo de {passo} em {passo}')
    for c in range(inicio,fim,passo):
      print(f'{c} ',end = '')
      
      

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)