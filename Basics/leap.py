n=int(input('enter a year->'))
if n % 4 == 0:
    if n % 100 == 0:
       if n % 400 == 0:
           print("{}is a leap year:{} ",format(n))
       else :
            print('{0} is not a leap year ',format(n))
    else :
         print('{0} is a leap year ',format(n))
else:
    print('{0} is not a leap year ',format(n))
