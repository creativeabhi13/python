#n=int(input('enter a number'))

#for  i in range(1,n+1):
 #   n*=i
#print(n)

def factorial(x):
    fact=1
    for i in range(1,x+1):

         fact*=i

    print(fact)

n=int(input("enter the number->"))
factorial(n)
