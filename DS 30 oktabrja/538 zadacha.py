total = 0
summ = 0
for c in range(1, 101):
    summ = summ + (1 / c)
print(summ)

for q in range(1, 101):
    if q % 2 == 1:
        total = total + (1 / q)
    if q % 2 == 0:
        total = total - (1 / q)
print(total)
