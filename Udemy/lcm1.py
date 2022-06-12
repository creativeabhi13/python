def lcm(a,b):
    m=a
    n=b
    while a!=b:
        if a>b:
            return b+n
        else:
            return a+m
    return a,b
a=int(input("Enter the First Number\n"));
b=int(input("Enter the Second Number\n"));
l=lcm(a,b)
print("lcm",l)