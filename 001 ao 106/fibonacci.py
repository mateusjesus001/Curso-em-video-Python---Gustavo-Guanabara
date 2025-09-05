termos = int(input('quantos termos vc quer ver:  '))
cond = 1
termo1 = 0
termo2 = 1
seguinte = 0
cond2 = 0
while cond <= termos:
  if cond2 == 0:
    print(termo1,'>',end = '')
    cond+=1
    print(termo2,'>',end = '')
    cond +=1
    cond2 = 1
  else:
    seguinte = termo1+termo2
    termo1,termo2 = termo2,seguinte
    print(seguinte,end = '')
    print(' >' if cond < termos else '', end = '')
    cond+=1
    