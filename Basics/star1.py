# printing the star
n = int(input('enter the number of row ->'))
for i in range(0, n, 2):
    for j in range(0, i + 1):
        print("*", end=' ')
    print('\n')

