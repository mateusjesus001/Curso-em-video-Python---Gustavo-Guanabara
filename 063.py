termos = int(input('quantos termos vc quer ver:  '))
cond = 1
termo1 = 0
termo2 = 1
seguinte = 0
cont = 0
while cond <= termos:
 if cont == 0:
  print(termo1,'>',end = '')
  termo1 = 1
  cond +=1
  print(termo1,'>',end = '')
  print(termo1,'>',end = '')
  cond+=2
  cont = 1
 else:
    seguinte = termo1+termo2
    termo1,termo2 = termo2,seguinte
    print(seguinte,end = '')
    print(' >' if cond < termos else '', end = '')
    cond+=1
  
 