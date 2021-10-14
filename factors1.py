def print_factors(n):
  print("the factors of",n,"are")
  for i in range(1,n+1):
      if n%i==0:
       print(i)
n=int(input('enter the number:'))
print_factors(n)
