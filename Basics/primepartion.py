def primecheck(m):
    c=0
    for i in range(2,m):
        if m%i==0:
            c+=1

    if c == 0:
        return True
    else:
        return False
def partition(m):
    l=[1]
    for i in range(2,m+1):
        if primecheck(i):
           l.append(i)


    for i in l:
        for j in l:
            if i+j==m:
               return True

    return False
print(partition(7))


