
def fib(num):
    assert num>=0 and int(num)==num, 'fibonacci series should be inteeger!'
    if num in [0,1]:
        return 1
    else:
        return fib(num-1)+fib(num-2)
print(fib(10))