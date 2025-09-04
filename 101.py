def voto(idade):
    if idade >= 18 and idade < 65:
     return True
    else:
     return False
ano = int(input('Digite o ano do seu nascimento: '))
idade = 2024 - ano
if voto(idade):
  print(f'Com {idade} anos: Voto obrigatório ')
else:
  print(f'Com {idade} anos: Voto opcional ')