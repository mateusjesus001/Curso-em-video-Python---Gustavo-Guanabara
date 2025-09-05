termo = int(input('digite o primeiro termo:  '))
razao = int(input('digite a razão da PA:  '))
limite = termo+(10-1)*razao
for c in range(termo,limite+1,razao):
    print(c, end = '>')
    