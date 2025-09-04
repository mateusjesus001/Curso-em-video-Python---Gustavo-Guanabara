print(f'------Tabuada------')
while True:
    num = int(input('digite um valor:  '))
    if num < 0:
        break
    for c in range(1,11,1):
        print(f'{num}x{c} = {num*c}')
    print('-'*20)