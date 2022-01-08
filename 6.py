def lcm(x,y):
    if x>y:
        lcm=x
    else:
        lcm=y
    while True:

        if (lcm % x == 0 and lcm % y == 0):
            break
        else:
            lcm = lcm + 1
    print(lcm)





a=int(input("enter the first number->"))
b=int(input("enter the second number->"))
lcm(a,b)