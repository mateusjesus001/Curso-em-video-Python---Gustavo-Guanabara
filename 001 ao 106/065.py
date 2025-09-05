resposta = 'S'
cont = acum = media = maior = menor = 0

while resposta == 'S':
 num = float(input('digite um número: '))
 cont += 1
 acum += num
 resposta = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
 media = acum/cont
 if cont == 1:
  maior = menor = num
 else:
  if num > maior:
   maior = num
  elif num < menor:
   menor = num
  
print(f'Vc digitou {cont} números e a média foi {media}')
print(f'O menor número foi {menor} e o maior número foi {maior}')
