from uteis import moeda


p = float(input('Digite o preço R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Diminuindo em 10% {p} temos {moeda.diminuir(p,10)}')
print(f'Aumentando em 50% {p} temos {moeda.aumentar(p,50)}')
