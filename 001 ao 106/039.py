nascimento = int(input('em que ano vc nasceu ?  '))
anoatual = 2023
if nascimento < anoatual:
  if nascimento + 18 < anoatual:
    idade = anoatual - nascimento
    alistamento = nascimento + 18
    ano_alistamento = alistamento - nascimento
    falta = 2023 - alistamento
    print(f' quem nasceu em {nascimento} tem {idade} anos em {anoatual}\n alistamento em {alistamento}\n vc deveria ter se alistado há {falta} anos')
  elif nascimento + 18 == anoatual:
     idade = anoatual - nascimento
     alistamento = nascimento + 18
     ano_alistamento = alistamento - nascimento
     print(f' quem nasceu em {nascimento} tem {idade} anos em {anoatual}\n alistamento em {alistamento}\n precisa se alistar imediatamente')
  else:  
     idade = anoatual - nascimento
     alistamento = nascimento + 18
     falta = alistamento - 2023
     print(f'quem nasceu em {nascimento} tem {idade} anos em {anoatual}\n seu alistamento será em {alistamento}\n faltam {falta} anos para se alistar')
else:
  print('nem nasceu')

