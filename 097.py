def escrever(txt):
    tamanho = len(txt)+6
    print('-'*tamanho)
    print(f'{txt}'.center(tamanho))
    print('-'*tamanho)


escrever('Olá mundo')
escrever('Oi')
escrever('5')