import requests

def verificarconexão():
 try:
  resposta = requests.get('https://www.google.com/')
  resposta.raise_for_status()
  return True
 except requests.ConnectionError:
  return False
 

conexão = verificarconexão()
if conexão:
 print(f'\033[1;33mConsegui acessar o site do google com sucesso !\033[m')
else:
 print(f'\033[1;31mO site do google não está acesssível no momento !\033[m')
  


 
