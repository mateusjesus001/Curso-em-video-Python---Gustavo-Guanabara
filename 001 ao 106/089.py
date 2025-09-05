list = []
pessoas = []
notas = []
while True:
 nome = input('Digite seu nome: ')
 nota1 = float(input('Digite a primeira nota: '))
 nota2 = float(input('Digite a segunda nota: '))
 notas.append(nota1)
 notas.append(nota2)
 pessoas.append(nome)
 pessoas.append(notas[:])
 list.append(pessoas[:])
 notas.clear()
 pessoas.clear()
 resposta = input('Quer continuar ? [S/N] ')
 if resposta in 'Nn':
  break
print('-='*50)
print('No.NOME     MÉDIA')
print('-'*50, end = '')
for c in list:
 print()
 print(f'{list.index(c)} {c[0]:<15}', end = '')
 print(f'{(c[1][0]+c[1][1])/2:.1f}', end = '')
print()
print('-'*50, end = '')
print()
while True:
 aluno = int(input('Mostrar as notas de qual aluno ? digite 999 para encerrar '))
 if aluno != 999:
  if aluno >= 0 and aluno < len(list):
   print(f'Primeira nota: {list[aluno][1][0]} Segunda nota: {list[aluno][1][1]}')
  else:
    print('Não existe essa posição de aluno na lista, digite um número válido')
 else:
  break
