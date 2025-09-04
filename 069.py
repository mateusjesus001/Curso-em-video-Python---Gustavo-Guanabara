mais_18 = homens = mulheres_20 = 0
while True:
 nome = str(input('Digite seu nome: '))
 idade = int(input('Digite sua idade: '))
 sexo = str(input('Digite seu sexo [M/F]: ')).upper()[0]
 while sexo not in 'MF':
  sexo = str(input('Sexo inválido, digite seu sexo [M/F]: ')).upper()[0]
 if sexo == 'M':
   homens += 1
 if idade > 18:
   mais_18 += 1
 if sexo == 'F':
   if idade < 20:
    mulheres_20 += 1
 continuar = str(input('Quer continuar ? [S/N]')).upper()[0]
 if continuar == 'S':
   True
 else:
   break
print(f'Há {mais_18} pessoas com mais de 18 anos cadastradas\nHá {homens} homens cadastrados\nE há {mulheres_20} mulheres com menos de 20 anos cadastradas')
