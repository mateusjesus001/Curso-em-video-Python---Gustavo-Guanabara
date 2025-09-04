def maior(*num):
    maior = cont = 0
    for c in num:
     if cont == 0:
      maior = c
      cont = 1
     else:
       if c > maior:
         maior = c
    print(f'Vc informou {len(num)} valores e o maior valor foi {maior}')


maior(2,3,999,5)    