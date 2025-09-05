import json

def salvar_dicionario(dicionarioper, dados):
    with open(dados, 'w') as arquivo:
        json.dump(dicionarioper, arquivo)

def carregar_dicionario(dados):
    try:
        with open(dados, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    
def leiaint(txt):
 while True:
  cond1 = 0
  cont1 = 0
  pergunta = input(txt)
  if pergunta != '':
   primeiroitem = pergunta[0]
   for c in pergunta:
    if c in ' abcdefghijklmnopqrstuvwxzy,.':
     cont1 += 1
   if cont1 >= 1:
    print(f'\033[1;31;40mErro digite um número inteiro !\033[;;m')
    cond1 = 1
   if primeiroitem in '0123456789-1-2-3-4-5-6-7-8-9' and cond1 == 0:
    return pergunta
  else:
   print(f'\033[1;31;40mErro digite um número inteiro !\033[;;m')




def verpessoas(dicionario):
   if dicionario == {}:
    print('-'*40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('-'*40)
    print('Nenhuma pessoa cadastrada até o momento')
   else:
     print('-'*40)
     print('PESSOAS CADASTRADAS'.center(40))
     print('-'*40)
     for k,v in dicionario.items():
       print(f'{k}               \t{v}')


def cadastrarpessoa(dicionario):
  nome = input('Nome: ')
  idade = leiaint('idade: ')
  print(f'Novo registro de {nome} adicionado')
  dicionario[nome] = f'{idade} anos'
  salvar_dicionario(dicionario,'arquivopermanente')

      
def menu():
   pessoas = carregar_dicionario('arquivopermanente')
   while True:
    print('-'*40)
    print('MENU'.center(40))
    print('-'*40)
    print(f'\033[1;33m1-\033[1;34mVer pessoas cadastradas\033[m')
    print(f'\033[1;33m2-\033[1;34mCadastrar nova pessoa\033[m')
    print(f'\033[1;33m3-\033[1;34mSair do programa\033[m')
    opção = input(f'\033[1;33mSua opção: \033[m')
    if opção == '1':
      verpessoas(pessoas)
    elif opção == '2':
      cadastrarpessoa(pessoas)
    elif opção == '3':
      print('-'*40)
      print('Saindo do sistema... até logo!'.center(40))
      print('-'*40)
      break
    else:
      print(f'\033[1;31mOpção inválida ! Digite novamente\033[m')
menu()
