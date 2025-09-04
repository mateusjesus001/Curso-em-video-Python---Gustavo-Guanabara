tupla = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')
palavra = ''
vog = ''
for item in range(0,len(tupla)):
  palavra = tupla[item]
  for c in palavra:
    if c in 'aeiou':
      vog += c
      vog += ' '
  print(f'Na palavra {palavra} temos {vog} ')
  vog = ''
      