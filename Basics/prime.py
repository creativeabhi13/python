#n=int(input('enter a number'))
#for i in range(2,n):
  #  if n%i==0:
 #       print("Not a prime no")
 #       break
  #  else:
 #       print("Prime no")
  #      break
#
def prime(x):
    for i in range(2,x):
        if x%i==0:
            print("not a prime")
            break
        else:
             print("prime")
             break
n = int(input("enter her number->"))

prime(n)
