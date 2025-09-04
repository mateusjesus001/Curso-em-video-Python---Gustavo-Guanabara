from random import randint
from time import sleep
cond = 0
cont = 0
print('-=-=-=Jogo-da-Advinhação=-=-=-')
while cond == 0:
 comp = randint(1,3)
 print('-=-=-=-=Estou-Pensando=-=-=-=-' )
 sleep(2)
 jog = int(input('Digite um número de 1 a 3:  '))
 if 0 <= jog < 4:
    print(f'O número que vc pensou foi 3{jog}? ')
    if comp == jog:
        print('Sim vc acertou')
        cond = 1
    else:
        print('Não\nTente denovo')
        cont+= 1
 else:
    print('número inválido tente denovo')
print(f'Vc levou {cont} tentativas para conseguir' )
