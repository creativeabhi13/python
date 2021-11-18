g=["mobile","laptop",100,"camera",310.28,"speakers",27.00,"television",1000]
str=[]
num=[]
for item in g:
         if type(item) == int or type(item)==float:
               num.append(item)
         else:
               str.append(item)
print(num)
print(str)

num.sort()
print(num)
num.reverse()
print(num)
str.sort()
print(str)
str.reverse()
print(str)
