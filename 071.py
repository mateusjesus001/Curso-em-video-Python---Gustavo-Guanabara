n50 = n20 = n10 = n1 = 0
valororiginal = int(input('digite um valor a ser sacado: '))
valor = valororiginal
while True:
 while valor >= 50:
  n50 +=1
  valor -= 50
 while valor >= 20:
  n20 +=1
  valor -= 20
 while valor >= 10:
  n10 +=1
  valor -= 10
 while valor >= 1:
  n1 += 1
  valor -= 1
 if valor < 1:
  break
print(f'sua quantia foi de R${valororiginal} e vc precisou de {n50} notas de 50\n{n20} notas de 20\n{n10} notas de 10\nE {n1} notas de 1 R$')
  
