num = int(input('Enter the number'))
if num <  1:
    print('enter the positive number')
else:
    sum =0
    while num>0:
        sum+=num
        num-=1
    print("the sum is",sum)
