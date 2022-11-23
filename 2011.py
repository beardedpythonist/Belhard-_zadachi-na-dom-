# #  задача 9,145
# s = '1 + 4 + 6 + 7 + 10'
# s = s.replace(' ', '')
# ls = s.split('+')
# for c in range(len(ls)):
#     ls[c] =  int(ls[c])
# x = sum(ls)
# print(x)

# #  задача 9,146
# s = '150 - 5 + 11 - 25 + 33'
# ls = s.split()
# for c in range(len(ls)):
#     if ls[c] != '-' and ls[c] != '+':
#         ls[c] = int(ls[c])
# for c in range(len(ls)):
#     if ls[c] == '-':
#         ls[c + 1] = ls[c + 1] * -1
# while '+' in ls:
#     ls.remove('+')
# while '-' in ls:
#     ls.remove('-')
#
# print(sum(ls))

## задача 9,184
# s = '0()000'
# count = 0
# for c in range(len(s)):
#     if s[c] == '(':
#         count += 1
#     if s[c] == ")":
#         count -= 1
#     if c == len(s) - 1 and count >= 1:
#         print('расставлены неверно, количество неверных открывающих скобок:', count)
#         break
#     if count < 0:
#         print('расставлены неверно, позиция первой неверной закрывающей скобки:', c)
#         break
# else:
#     print('расставлены верно')
#
