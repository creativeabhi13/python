n=int(input("lenght of the list-> "))
a=[]
print("enter the element of list->")
for i in range(n):

    a.append(int(input()))
print(a)
print("enter the number of iteration->")
x=int(input())
for i in range(x):
        x=a.pop(0)
        a.append(x)
        print(a)