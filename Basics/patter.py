# printing the star
n = int(input('enter the number of row ->'))
for i in range(1, n+1, 2):
    for j in range(1, i + 1):
        if i<=n-j:
              print(" ")
        else:
              print("*",end=" ")
    print('\n')

