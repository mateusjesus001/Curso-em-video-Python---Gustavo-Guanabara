masc = fem = 0
tot = 0
fem_menor_20 = 0
homem_mais_velho = 0
nomemaisvelho = 0
total_idade = 0
media = 0
mascv = 0
femv = 0
for c in range(0,4):
    nome = str(input('nome: '))
    idade = int(input('idade: '))
    sexo = str(input('sexo: F/M  ')).strip().upper()
    total_idade += idade
    if sexo == 'M':
     if c == 0:
      homem_mais_velho = idade
     else:
       if idade > homem_mais_velho:
         homem_mais_velho = idade
         nomemaisvelho = nome
         mascv = 1
    if sexo == 'F':
      if idade < 20:
       fem_menor_20 +=1
       femv = 1
media = total_idade/4
print(f'A média de idade do grupo é de {media}anos')
if mascv != 0:
  print(f'O homem mais velho tem {homem_mais_velho} anos e se chama {nomemaisvelho}')
if femv != 0:
  print(f'Ao todo são {fem_menor_20} mulheres menores de 20 anos')
     
