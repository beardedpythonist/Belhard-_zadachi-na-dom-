import math

s_kr = float(input())
s_kw = float(input())
r = (s_kr / math.pi) ** 0.5
d = 2 * r    # нахождение диаметра круга
a = s_kw ** 0.5

c = (a ** 2 + a ** 2) ** 0.5     # гипатенуза т.е. диаганаль квадрата

if d > c:
    print('квадарт можно вместить в круг')
if c > d:
    print('круг можно вместеть в квадрат')

print(d)
print(c)
