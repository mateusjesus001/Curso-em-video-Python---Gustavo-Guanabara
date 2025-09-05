jogador = {}
gols = []
total = 0
cont = 1
nome = input('Digite seu nome: ')
partidas = int(input('Quantas partidas vc jogou: '))
for c in range(partidas):
 golsporpartida = int(input(f'Digite os gols da {cont}ª partida '))
 gols.append(golsporpartida)
 cont += 1
cont = 1
jogador['Nome'] = nome
jogador['Gols'] = gols
for item in gols:
 total += item
jogador['Total'] = total
print(jogador)
print('-='*30)
for k,v in jogador.items():
 print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {nome} jogou {partidas} partidas')
for c in range(0,partidas):
 print(f'> Na partida {cont},fez {jogador["Gols"][c]} gols', end = '')
 cont += 1
 print()
print(f'Foi um total de {total} gols')