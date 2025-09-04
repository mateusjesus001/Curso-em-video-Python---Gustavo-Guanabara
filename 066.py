cont  = acum = 0
while True:
 num = int(input('digite um número: '))
 if num == 999:
  break
 cont += 1
 acum += num
print(f'Vc digitou {cont} números e a soma deles é {acum}')