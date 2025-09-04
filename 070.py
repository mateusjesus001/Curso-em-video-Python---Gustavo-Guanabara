soma = mais_de_1000 = maisbarato = nomebarato = cont = 0
while True:
 produto = str(input('Digite o produto a ser comprado: '))
 preço = float(input('digite o preço do produto: '))
 soma += preço
 if preço > 1000:
  mais_de_1000 += 1
 cont +=1 
 if cont == 1:
  maisbarato = preço
  nomebarato = produto
 else:
  if preço < maisbarato:
   maisbarato = preço
   nomebarato = produto
 resposta = str(input('Quer continuar ? [S/N]')).upper()[0]
 if resposta == 'S':
  True
 else:
  break
print(f'Vc gastou no total R${soma:.2f}\nTem {mais_de_1000} produtos valendo mais de R$1000\nE o produto mais barato foi {nomebarato} custando R${maisbarato}')
 
