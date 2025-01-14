# lcm of two number
a = int(input('enter the first number->'))
b = int(input('enter the second number->'))
if a>b:
    lcm = a
else:
    lcm = b

while True:
    if lcm%a==0 and lcm%b==0:
        break
    else:
        lcm = lcm + 1

print("\nLCM =", lcm)