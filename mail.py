

n = 9123
def obr(n):
    while n > 0:
        x = n % 10
        print(x)
        obr(n // 10)
        return


obr(n)
