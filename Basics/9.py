def fabonaci(n):
       if n<=1:
            return n
       else:
            return fabonaci(n-1)+fabonaci(n-2)

n=int(input("enter the number->"))
if n<=0:
    print("please enter the postive number")
else:
    print("the fibonacci series are")
    for i in range(n):
        print(fabonaci(i))