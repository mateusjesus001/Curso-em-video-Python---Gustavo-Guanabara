nome = input('Qual é o seu nome? ')
posicao = nome.find('Silva')

if posicao != -1:
    print(f'O sobrenome "Silva" começa na posição {posicao} na string do nome.')
else:
    print('O sobrenome "Silva" não foi encontrado no nome.')
