list = []
pessoas = []
cont = maior = menor = cont2 = 0
while True:
 pessoas.append(str(input('Digite seu nome: ')))
 pessoas.append(float(input('Digite seu peso: ')))
 list.append(pessoas[:])
 pessoas.clear()
 cont += 1
 resposta = input('Quer continuar ? [S/N] ')
 if resposta in 'Nn':
  break
print(f'Foram cadastradas {cont} pessoas')
for c in list:
 if list.index(c) == 0:
  maior = menor = c[1]
 else:
  if c[1] > maior:
   maior = c[1]
  if c[1] < menor:
   menor = c[1]
print(f'As pessoas mais pesadas tem ', end = '')
for d in list:
  if d[1] == maior:
    if cont2 == 0:
     print(f'{d[1]}Kg. Peso de [{d[0]}]', end = '')
     cont2 = 1
    else:
     print(f'[{d[0]}]', end = '')
print()
print(f'As pessoas mais leves tem ', end = '')
for z in list:
  if z[1] == menor:
   if cont2 == 1:
    print(f'{z[1]}Kg. Peso de [{z[0]}]', end = '')
    cont2 = 2
   else:
    print(f'[{z[0]}] ', end = '')