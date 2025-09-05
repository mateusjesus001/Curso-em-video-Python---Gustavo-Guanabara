list = []
listaprincipal = []
cont = cont2 = 1
indice = 0
while True:
 total = 0
 jogador = {}
 gols = []
 nome = input('Digite seu nome: ')
 partidas = int(input('Quantas partidas vc jogou: '))
 for c in range(partidas):
  golsporpartida = int(input(f'Digite os gols da {cont}ª partida '))
  gols.append(golsporpartida)
  cont += 1
 cont = 1
 jogador['Nome'] = nome
 jogador['Gols'] = gols[:]
 for item in gols:
  total += item
 jogador['Total'] = total
 list.append(jogador.copy())
 del(gols)
 del(jogador)
 resposta = input('Deseja contiuar ? [S/N] ')
 if resposta in 'Nn':
  break
print('-='*30)
print('Code nome  Gols  Total')
print('-='*30)
for item in list:
 valores = []
 for v in item.values():
  valores.append(v)
 listaprincipal.append(valores[:])
for i,v in enumerate(listaprincipal):
 print(f'{i}   {v[0]}   {v[1]}    {v[2]}', end = '')
 print()
 indice += 1
print('-='*30)
while True:
 dados = int(input('Mostrar dados de qual jogador ? Digite 999 para sair '))
 if dados != 999:
  if dados >= 0 and dados < len(listaprincipal):
   print(f'Levantamento do jogador {listaprincipal[dados][0]}:')
   for i in listaprincipal[dados][1]:
    print(f'Na {cont2}ª partida fez {i} gols')
    cont2 += 1
   cont2 = 1
  else:
   print('Não existe um jogador no cadastro referente a essa posição, digite uma posição válida')
 else:
  break