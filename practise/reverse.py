n=int(input("Enter the number"))
num=n
while num>0:
    last_digit=num%10
    print(last_digit,end="")
    num=num//10
print()

# Time complexity: O(log n)
# Space complexity: O(1)

# 1. Using recursion
def reverse(num):
    if num==0:
        return
    else:
        last_digit=num%10
        print(last_digit,end="")
        reverse(num//10)
print()
reverse(n)
# Time complexity: O(log n)
# Space complexity: O(log n) due to recursion stack