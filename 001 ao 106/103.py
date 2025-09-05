def ficha(n= 'desconhecido',g= 0):
 if n == '':
  n = 'desconhecido'
 if g == '' or g[0] not in '0123456789':
  g = 0
 print(f'O jogador {n} fez {g} gols no campeonato')

    
jogador = input('Nome do Jogador: ').strip()
gols = input('Número de Gols: ')

ficha(jogador,gols)
