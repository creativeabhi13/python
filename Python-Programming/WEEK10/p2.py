#find the number of digits in a given number
n=int(input("enter the number"))
num=str(n)
digits=0
for c in num:
    digits=digits+1
print(digits)