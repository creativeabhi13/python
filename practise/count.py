n=int(input("Enter the number: "))
num=n
count=0
while num>0:
    last_digit=num%10
    count+=1
    num=num//10
print(count)

#  Time complexity: O(log n)
# Space complexity: O(1)
from math import *
def count1(num):
    return int(log10(num))+1 # log10(n) gives the number of digits in n
#  Time complexity: O(1)

print(count1(n))