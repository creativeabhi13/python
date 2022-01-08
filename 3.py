import cmath
a=int(input("enter the coefficient of a->"))
b=int(input("enter the coefficient of b->"))
c=int(input("enter the coefficient of c->"))
d=b*2-4*a*c
if d==0:
    print("the roots are real and equal")
    root1=root2=-b/2*a+(d**1/2)/2*a
elif d>0:
    print("the roots are real and distinct")
    root1 = (-b / 2 * a + (d ** 1 / 2) / 2 * a)
    root2 = (-b / 2 * a - (d ** 1 / 2) / 2 * a)
else:
    print("the roots are imaginary")
    root1 = -b / 2 * a + (cmath.sqrt(d)) / 2 * a
    root2 = -b / 2 * a - (cmath.sqrt(d)) / 2 * a
print(root1)
print(root2)