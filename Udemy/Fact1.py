def factorial(n):
    assert n >= 0 and int(n) == n, 'This only positive numbers are allowed'
    if n in [0,1]:
        return 1

    return n * factorial(n-1)
print(factorial(4))
