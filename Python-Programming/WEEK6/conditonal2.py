#find whther the given number ends with 0 or 5..
print("enter the number")
n=int(input())
if n%5== 0:
  if n%10==0:
     print("0" +" " +" the number is divisible by 10")
  else:
     print("5"+" " +" the number is divisible by 5")
else:
   print("other" +" " +" the number is not divisible by 5 or 10")
  