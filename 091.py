from random import randint
from time import sleep
from operator import itemgetter
dict = {'jogador1': randint(1,6),'jogador2': randint(1,6),'jogador3': randint(1,6),'jogador4': randint(1,6)}
for k,v in dict.items():
 print(f'O {k} tirou {v}')
print('-='*30)
ranking = sorted(dict.items(), key=itemgetter(1), reverse = True)
ranking = list(ranking)
for i,v in enumerate(ranking):
 print(f'{i+1}ª lugar {v[0]} com {v[1]}')


