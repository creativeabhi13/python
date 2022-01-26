# find the number of digit in the given numbers
n=int(input("Enter the number: "))
digit=1
while n>9:
  n=n//10
  digit=digit+1
print(digit)