maior = menor = 0
for c in range(0,5,1):
 peso = float(input('Digite seu peso:  '))
 if c == 0:
  maior = menor = peso
 if c != 0:
  if peso > maior:
   maior = peso
  if peso < menor:
   menor = peso
print(f'O maior peso foi {maior} e o menor peso foi {menor}')

