x = float(input('введите курс долл к рублю '))

for c in range(1, 21):
    okr = round(x * c, 2)
    print(c, 'долларов равно:', okr)
    
