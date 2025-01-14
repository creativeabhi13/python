num=int(input('enter the number'))
if num < 0:
   print('enter the postive number')
else:
     sum=0
     for i in range(1,num+1):
            sum+=i
     print(sum)
