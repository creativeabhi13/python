n = int(input(""))


def sumof(n):
    assert n >= 0 and int(n) == n, 'This is only for postiive number '
    if n == 0:
        return 0
    else:
        return int(n % 10)+sumof(int(n/10))


print(sumof(n))
