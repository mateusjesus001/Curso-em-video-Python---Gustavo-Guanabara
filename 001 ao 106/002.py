cadastro_insumos_de_embalagem = []
pausar = 0
while pausar == 0:
 insumos_De_Embalagem = input('insumo de embalagem pra inserir: ')
 cadastro_insumos_de_embalagem.append(insumos_De_Embalagem)
 parar = input('deseja parar ? S/N  ').upper()
 if parar == 'N':
  pausar = 0
 else:
  pausar = 1