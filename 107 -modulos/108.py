from uteis import moeda


p = float(input('Digite o preço R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Diminuindo em 10%, {moeda.moeda(p)} temos {moeda.moeda(moeda.diminuir(p,10))}')
print(f'Aumentando em 50%, {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentar(p,50))}')
