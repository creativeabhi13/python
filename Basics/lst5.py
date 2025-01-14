# write a python program to check a list is sorted or not
a = [8,7,6,5,4,3]
print("original list:"+ str(a))
flag=0
i=1
while i<len(a):
      if a[i]>a[i-1] or a[i]<a[i-1]:
          flag = 1
      i=i+1


if flag==1:
    print("the list is sorted ")
else:
    print("the list is not sorted")