# функция , рекурсия

# 10.33

# def ris():
#     print('******************************************************************************************************')
## 10.34
#
# s = '*'
# for c in range(101):
#     print(s, end='')
# for c in range(10):
#     print(s, '                                                                                                  ', s)
# for c in range(101):
#     print(s, end='')

# def ris():
#     print('******************************************************************************************************')
# s =  '*'
# ris()
# for c in range(10):
#     print(s, '                                                                                                  ', s)
# ris()
#
# 10.35
# def risver(n):
#     for c in range(n):
#         print('*', end='')
# risver(int(input()))


# 10.36
# def risver(n):
#     for c in range(n):
#         print('*', )
# risver(int(input()))

# 10.37 a
# s = '*'
# n = int(input('введите число: '))
# print(s * n)
# for c in range(n):
#     print(s + ' ' * (n - 2) + s)
# print(s * n)
#
# 10.37 б
# def prjamougl(n):
#     s = '*'
#     print(s * n)
#     for c in range(n):
#         print(s + ' ' * (n - 2) + s)
#     print(s * n)
#
# x = int(input('Введите число:'))
# prjamougl(x)


# 10.38
# def obmen(a, b, c, d):
#     a, b = b, a
#     c, d, = d, c
#     return a, b, c, d
#
# x = 5
# y = 10
# z = 100
# w = 1000
# print(obmen(x, y, z, w))

# 10.39

# def treug(a,b,c):
#     per = a + b + c
#     s = (a + b + c) / 2
#     print(per, s)
#     return per, s
# a1 = 5
# b1 = 4
# c1 = 6
#
# a2 = 8
# b2 = 9
# c2 = 10
# per, s = treug(a1, b1, c1)
# per2, s2 = treug(a2, b2, c2)
# per_total = per + per2
# s_tot = s + s2
# print(per_total, s_tot)


#10.40
# def trapets(a, b, h):
#     s = ((a + b) / 2) * h
#     c = (b - a) / 2
#     per = a + b + 2 * ((h**2 + c**2)**0.5)
#     print(s, per)
#     return s, per
# s1, per1 = trapets(5, 7, 6)
# s2, per2 = trapets(6, 9, 8)
# s_sum = s1 + s2
# per_sum = per1 + per2
# print(s_sum, per_sum)