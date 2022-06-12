def lcm(a,b):
    if a>b:
        lcm=a
    else:
        lcm=b
    while True:
        if lcm%a==0 and lcm%b==0:
            break
        else:
            lcm=lcm+1
    print(lcm)

a=int(input("Enter the first number\n"))
b=int(input("Enter the second number\n"))
lcm(a,b)
