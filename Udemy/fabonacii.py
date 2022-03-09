def fibonacii(n):
    assert n>=0 and int(n) == n, "Fibonacci cannot be negative integer."
    if n in [0,1]:
        return n
    else:
        return fibonacii(n-1)+fibonacii(n-2)
print(fibonacii(5))