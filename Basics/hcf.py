# Hcf of two number
a = int(input('enter the first number->'))
b = int(input('enter the second number->'))
if a>b:
    Hcf = a
else:
    Hcf = b

while True:
    if a%Hcf==0 and b%Hcf==0:
        break
    else:
        Hcf = Hcf - 1

print("\nHCF =", Hcf)