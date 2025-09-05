list = []
for c in range(0,5):
    num = int(input('digite um número: '))
    if c == 0:
        list.append(num)
        maior = menor = num
        print('Adicionado no final da lista')
    else:
     if num > maior:
        list.append(num)
        maior = num
        print(f'Adicionado no final da lista')
     if num < menor:
        list.insert(0,num)
        menor = num
        print(f'Adicionado na posição {list.index(num)}')
     if num < maior and num > menor:
        list.insert(list.index(maior),num)
        print(f'Adicionado na posição {list.index(num)}')
print(list)
