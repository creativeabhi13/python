# for reverse a number
import string
n=int(input("enter the number:-"))
num=str(n)
rev=""
for c in num:
  rev = c + rev
if n>=0:
  print(rev)
else:
  print("-"+rev)
