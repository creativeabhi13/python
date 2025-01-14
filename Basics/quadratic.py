import cmath
a = int(input('enter the first coeffiecient of a->'))
b = int(input('enter the second coefficeint of b->'))
c = int(input('enter a contant value function->'))
d = b**2-4*a*c
if d==0:
        print('Real and equal\n')
        root1 = root2 = -b/2*a
elif d>0:
         print('Real and distinct\n')
         root1 = -b/2*a + (sqrt(d))/2*a
         root2 = -b/2*a - (sqrt(d))/2*a
else:
         print('roots imaginary roots\n')
         root1 = -b/2*a + (cmath.sqrt(d))/2*a
         root2 = -b/2*a - (cmath.sqrt(d))/2*a
print('Roots are Root1->' ,root1,'Root2-> ' ,root2)