#palindrome
import string
n=int(input("enter the number:-"))
num=str(n)
rev=""
for c in num:
  rev = c + rev
if n<=0:
  rev = '-'+rev
if(n== int(rev)):
  print("palindrome")
else:
  print("not a plaindrome")

