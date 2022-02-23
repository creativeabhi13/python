num = int(input())
if num < 0:
    print("Enter a postiive a number")

else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print("The sum of n natural number is ", sum)