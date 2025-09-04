multa = 0
kmporhora = int(input('quantos km por hora ?'))
if kmporhora > 80:
 print('você foi multado')
 multa = (kmporhora-80)*7
 print(f'sua multa é de \33[31mR${multa:.2f}\33[m')



 