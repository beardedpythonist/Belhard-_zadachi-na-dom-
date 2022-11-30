
n = int(input())
x = n
summa = 0
for c in range(1, 2 * n + 1):
    summa = summa + (x ** 2)
    x = x + 1
    if x > 2 * n:
        break
print(summa)

