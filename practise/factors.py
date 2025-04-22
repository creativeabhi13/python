# calculate the factors of a number

from math import sqrt

n=int(input("Enter the number:"))
num=n

result=[]

for i in range(1,int(sqrt(num))+1):
    if num%i==0:
        result.append(i)
        if i!=num//i:
            result.append(num//i)
result.sort()
print("The factors of the number are:",result)

# Time complexity: O(sqrt(n))
# Space complexity: O(sqrt(n))