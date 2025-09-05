cond = 0
while  cond == 0:
    resposta = str(input('Digite seu sexo [F/M]:  ')).strip().upper()
    if resposta != 'F' and resposta != 'M':
        print('letra inválida')
    else: 
     cond = 1
     print('acertou')