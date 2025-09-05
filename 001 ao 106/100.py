from random import randint
lista = []
def sortearlista():
    for c in range(0, 5):
        lista.append(randint(1, 50))
    print(lista)


def somaparlista(lst):
    somapar = 0
    for c in lst:
        if c % 2 == 0:
            somapar += c
    print(f'A soma dos valores pares de {lst} é {somapar}')

sortearlista()
somaparlista(lista)
