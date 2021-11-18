#logical and ->both condition should be true
#logical or ->any one is true then true
a=int(input("enter the first number->"))
b=int(input("enter the second number->"))
c=int(input("enter the Third number->"))
if a == b and b != c:
    a=1
    b=2
    c=3
    print(a,b,c)
elif a ==b or b !=c :
    print("wrong data")
else:
    print("hi")
