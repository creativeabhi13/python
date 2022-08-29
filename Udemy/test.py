def factorial(num):
    assert num>=0 and int(num)==num, 'this is the exponential!'
    if num in [0,1]:
        return 1
    return num*factorial(num-1)
print(factorial(5))