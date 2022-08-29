n = int(input(""))

assert n >= 0 and int(n) == n, 'The number has to be a postive integer only!.'


def fib(n):
    if n in [0, 1]:
        return n
    else:
        return fib(n-1)+fib(n-2)


print(fib(n))
