# return true if a number is palindrome false if not palindrome
n=int(input("Enter the number:"))
num=n
rev=0
while num>0:
    last_digit=num%10
    rev=rev*10+last_digit
    num=num//10
if rev==n:
    print("true")
else:
    print("false")
# # Time complexity: O(log n)
# calculate the time complexity of the above code
 


# # Space complexity: O(1)

