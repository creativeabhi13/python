# reverse the Number
num=int(input("Enter the number:-"))
num1=(num)
if(num>=0):
  rev=num%10
  num=num//10
  while(num>0):
     rev1=num%10
     num=num//10
     rev=rev*10+rev1
  print(rev)
else:
   rev=num1%10
   num1=num1//10
   while(num1>0):
     r=num1%10
     num1=num1/10
     rev=rev*10+r
   print(rev - 2 * rev)
  
    
 