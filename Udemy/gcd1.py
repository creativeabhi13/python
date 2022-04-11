def gcd(a,b):
    while(a!=b):
        if a>b:
            return gcd(a-b,b)
        else:
            return gcd(a,b-a)
    return a,b
a=int(input("enter the First number\n"))
b=int(input("enter the second number\n"))
l=gcd(a,b)
print(l)