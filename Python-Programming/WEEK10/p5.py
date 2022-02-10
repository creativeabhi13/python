# Nested for loop
#find all the prie number less than entered number
n=int(input("enter the number:-"))
if n>2:
  print(2,end=" ")
for i in range(3, n):
  flag=False
  for j in range(2, i):
      if i%j==0:
        flag=False
        break
      else:
        flag=True
  if flag:
    print(i,end=" ")
    