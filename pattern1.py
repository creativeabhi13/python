row=int(input("enter the number of the row->"))
n=1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(n, end=" ")
        n = n + 1
    print('\n')

