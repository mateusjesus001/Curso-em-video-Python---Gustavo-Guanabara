list = [[],[]]
for c in range(0,7):
 num = int(input('Digite um número: '))
 if num %2 == 0:
  list[0].append(num)
 else:
  list[1].append(num)
print(sorted(list[0]))
print(sorted(list[1]))