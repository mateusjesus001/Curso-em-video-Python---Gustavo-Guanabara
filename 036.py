casa = float(input('qual o valor da casa ? '))
salário = float(input('qual o seu salário ? '))
anos = int(input('quantos anos vc ficará pagando ? '))
prestação = casa/(anos*12)
minimo = salário*30/100
if prestação < minimo:
  print('empréstimo aprovado')
else:
  print('empréstimo negado')
print(prestação)