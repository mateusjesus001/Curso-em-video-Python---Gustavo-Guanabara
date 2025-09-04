def fatorial(num, show = False):
    if show == True:
     for c in range(num,0,-1):
      if c > 1:
       print(f'{c} x ', end = '')
      else:
        print(f'{c} = ', end = '')
    f = 1
    while num > 0:
     f *= num
     num -= 1
    print(f)


fatorial(5)