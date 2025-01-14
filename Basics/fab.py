def fab(n):
    if n<=1:
        return False
    else:
         return fab(n-1)+fab(n-2)

n=(input("enter the number"))
a=fab(n)
print(a)