# extraction of digit from the given number amd show the number 
n=int(input("Enter the number: "))
num=n
while num>0:
    last_digit=num%10
    print(last_digit,end="")
    num=num//10
print()
#  Time complexity: O(log n)
# Space complexity: O(1)

