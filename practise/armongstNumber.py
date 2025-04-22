# Armstong number:- the sum of the cubes of the digits of a number is equal to the number itself.
n=int(input("Enter the number: "))
num=n
sum=0
nod=len(str(num))
while num>0:
    last_digit=num%10
    sum+=last_digit**nod
    num=num//10
if sum==n:
    print("true")
else:
    print("false")    

    # time complexity: O(log n)
    # space complexity: O(1)
