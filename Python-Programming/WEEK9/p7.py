#formatted print output
for i in range(11):
  print(i,end=" ")
d=10
m=2
y=2022
print("Today date is :",end=" ")
print(d,m,y, sep="/")

# multiplication of given number
num =int(input("enter a number:-"))
for i in range(1,11):
  #print(num, "X", i, '=', num*i)
#formatted print
  #print(f'{num} X {i} = {num * i}')
  #print('{0} X {1} = {2}'.format(num, i, num * i))
  print('%d x %d = %d' % (num, i, num*i))

pi=22/7
print(f'VALUE OF PI = {pi}')
print(f'VALUE OF PI = {pi:.2f}')
print('VALUE OF PI = {0}'.format(pi))
print('VALUE OF PI = %f' % (pi))

print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))

print('{0:5d}'.format(11111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(111))
print('{0:5d}'.format(11))
print('{0:5d}'.format(1))