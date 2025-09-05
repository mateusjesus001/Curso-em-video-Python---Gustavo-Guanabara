ptermo = int(input('digite o primeiro termo: '))
razão = int(input('digite a razão: '))
p = ptermo +(10-1)*razão
cond = False
n = 0
acum = 0
cont = 'S'
while not cond:
    if ptermo <= p:
     print(ptermo)
     ptermo = ptermo+razão
     acum = ptermo
    else:
       while cont == 'S':
        cont = str(input('Deseja mostrar mais números [S/N]')).strip().upper()[0]
        if cont == 'S':
            seq = int(input('quantos numéros da sequencia a mais vc quer exibir ?'))
            p = acum +(seq-1)*razão
            while not cond:
                if acum <= p:
                 print(acum)
                 acum = acum+razão
                else:
                 break
        else:
          cond = True
