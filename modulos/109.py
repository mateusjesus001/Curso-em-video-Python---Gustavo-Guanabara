from uteis import moeda2


p = float(input('Digite o preço R$'))
print(f'A metade de {moeda2.moeda(p)} é {moeda2.metade(p,True)}')
print(f'O dobro de {moeda2.moeda(p)} é {moeda2.dobro(p,True)}')
print(f'Diminuindo em 10% {moeda2.moeda(p)} temos {moeda2.diminuir(p,10,True)}')
print(f'Aumentando em 50% {moeda2.moeda(p)} temos {moeda2.aumentar(p,50)}')
