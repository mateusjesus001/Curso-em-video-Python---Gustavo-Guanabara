compras = float(input('Qual o valor das compras? '))
print(f'O preço das compras é R$ {compras:.2f}')
print('''Formas de Pagamento
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x no cartão''')

resposta = int(input('Qual a forma de pagamento? '))
preço = 0

if resposta == 1 or resposta == 2:
    preço = compras - 150
elif resposta == 3:
    preço = compras + compras * 0.1
elif resposta == 4:
    parcelas = int(input('Em quantas parcelas você deseja pagar? '))
    preço = (compras/parcelas) + (compras * 0.1) * parcelas
    prestação = compras/parcelas
    print(f'Sua compra será parcelada em {parcelas} de R$ {prestação} com juros')
else:
    print('Opção inválida')

if preço != 0:
    print(f'O valor a ser pago será de R$ {preço:.2f}')


