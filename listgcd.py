def gcd(x,y):
    a=[]
    b=[]
    for i in range(1,x+1):
        if x%i==0:
            a.append(i)
    for i in range(1,y+1):
        if y%i==0:
            b.append(i)
    c=[]
    for i in a:
              if i in b:
                  c.append(i)
    print(a)
    print(b)
    print(c)
    print(c[-1])
gcd(60,8)
