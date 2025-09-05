num = 1
cont = 0
acum = 0
while num != 999:
    num = int(input('digite um número:  '))
    if num != 999:
        cont +=1
        acum += num
print(f'Vc digitou {cont} números e a soma deles foi {acum}')
    