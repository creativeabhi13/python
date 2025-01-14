def gcd(x,y):
    if x>y:
        gcd=x
    else:
        gcd=y
    while True:

        if (x%gcd == 0 and y % gcd == 0):
            break
        else:
            gcd = gcd -1
    print(gcd)





a=int(input("enter the first number->"))
b=int(input("enter the second number->"))
gcd(a,b)