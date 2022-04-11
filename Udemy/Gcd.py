def gcd(a,b):
    if a>b:
        hcf=a
    else:
        hcf=b
    while True:
        if a%hcf==0 and b%hcf==0:
            break
        else:
            hcf=hcf-1
    print("\n hcf",hcf)
a=int(input("enter the first number\n"))
b=int(input("enter the second number\n"))
gcd(a,b)