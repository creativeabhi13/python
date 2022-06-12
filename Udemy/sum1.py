def recursiveRange(num):
    sum=0
    if num==0:
        return 0

    return num+recursiveRange(num-1)
print(recursiveRange(6))
