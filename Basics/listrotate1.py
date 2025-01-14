def rotate(l,k):
    if k==0:
        return l
    else:
        for i in range(k):
            temp = l[0]
            del l[0]
            l.append(temp)
            print(l)
    return l
l=[1,2,3,4,5]
a=rotate(l,5)


