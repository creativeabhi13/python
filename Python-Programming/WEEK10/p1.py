#for loop
# factorial of a given number
n=int(input("enter the number:-"))
fact=1
if n<0:
  print("not defined")
else:
  for i in range(n,1,-1):
      fact*=i
  print(fact)