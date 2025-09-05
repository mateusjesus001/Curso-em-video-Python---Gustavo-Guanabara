num = int(input('digite um valor: '))#usando for
tot = 0
for c in range(num,0,-1):
    if c!= 1:
     if c == num:
      tot = c*(c-1)
     elif c == num-1:
       tot = tot
     else:
       tot = tot*c
print(tot)

num = int(input('digite um valor:  '))#usando while
tot = 0
cond = 0
fat = 0
cond2 = 0
cond3 = 0
while cond ==0:
    if num > 1 and cond2 == 0 and cond3 == 0:
     tot = num*(num-1)
     num = num-1
     cond2 = 1
    if num > 1 and cond3 == 0:
     tot = tot
     num = num-1
     cond3 = 1
    if num > 1:
      tot = tot*num
      num = num-1
    else:
       cond = 1
print(tot)