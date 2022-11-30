
x = 2
summa  = 1

for c in range(1, 13):
    if c % 2 == 1:
        y =  ((c +1) / (c + 2)) * x  ** c
        summa = summa - y
    elif  c % 2 == 0:
        y = ((c + 1) / (c + 2)) * x ** c
        summa = summa + y
print(summa)

