def rotate(x,k):
    if k==0:
        return x
    else:

         for i in range (k):
             temp = x[0]
             del x[0]
             x.append(temp)
             print(x)
    return x
x=[1,2,3,4,5,6,7]
n=int(input("enter the number of rotation or iteration-> "))
rotate(x,n)
