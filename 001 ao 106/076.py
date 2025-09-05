listagem = ('pão','1','leite','3.50','frango','10.90')
print('-'*30)
print('Listagem de preço'.center(30))
print('-'*30)
for item in range(0,len(listagem),2):
    print(f'{listagem[item]}..........R${listagem[item+1]}')
print('-'*30)