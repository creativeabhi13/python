n = int(input(""))

assert n >= 0 and int(n) == n, 'The number has to be a postive integer only!.'


def fact(n):
    if n in [0, 1]:
        return 1
    else:
        return n*fact(n-1)


print(fact(n))
