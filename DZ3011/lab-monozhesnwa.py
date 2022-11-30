# 1задача
m1 = 'New job opportunities for many positions in our Company worldwide.'
m1 =set(m1)
print(m1)

# 2 задача
n = 6
mx = set()
ls = []
for c in range(1, n + 1):
    m = set(input())
    ls.append(m)
    if c % 3 == 0:
        q = ls[c - 1].difference(ls[0])
        print(q)

# задача про Вузы
mn = {'Диалог', 'Avicom', 'Нэта', 'Сервер', 'Декада', 'Dega'}
mn1 = {'Диалог', 'Avicom'}
mn2 = {'Avicom', 'Нэта', 'Сервер'}
mn3 = {'Диалог', 'Avicom', 'Нэта', 'Сервер'}

# каждый из вузов
total1 = mn1
print(total1)
# хотя бы один из вузов
mn_temp = mn1.union(mn2)
print(mn_temp)
# ни один из вузов
mn_razn = mn - mn_temp
print(mn_razn)