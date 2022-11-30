a = int(input())
b = int(input())
c = int(input())

d = b * 2 - 4 * a * c
if d > 0:
    print('Уравнение имеет 2 корня')
if d == 0:
    print(' есть один корень')
if d < 0:
    print('уравнение корней не имеет')
