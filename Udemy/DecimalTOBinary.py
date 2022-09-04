n = int(input("enter the number"))


def decimalToBinary(n):
    assert int(n) == n, 'The parameter must be integer only!'
    if n == 0:
        return 0
    else:
        return n % 2+10*decimalToBinary(int(n/2))


l = decimalToBinary(n)
print(l)
