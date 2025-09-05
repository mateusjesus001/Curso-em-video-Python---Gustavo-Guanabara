num = (input('digite um número inteiro de 4 digitos: '))
numdividido = list(num)
if len(numdividido)== 4:
 milhar = numdividido[0]
 centena = numdividido[1]
 dezena = numdividido[2]
 unidade = numdividido[3]
 print(f'a milhar é {milhar}')
 print(f'a centena é {centena}')
 print(f'a dezena é {dezena}')
 print(f'a uindade é {unidade}')
else:
 print('O número precisa ter 4 digitos')