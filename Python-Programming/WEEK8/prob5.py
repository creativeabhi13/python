#check whether the number is palondrome or not
#palindrome are those number if u reverse the number which u have entered u will get the same number so it is called palindrome.
n=int(input("enter the number:-"))
temp=n
result=0

while n!=0:
  r=n%10
  result=result*10+r
  n=n//10
print(result)
if(temp==result):
    print("a number is palinderome")
    
else:
    print("the number is not a palindrome")
    
