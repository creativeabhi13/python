# factorial of a number
#n=5
#1*2*3*4*5=120
n=int(input("enter a number:-\n"))
i=1
sum=1
while i<=n:
  sum*=i
  i=i+1
print(sum)
