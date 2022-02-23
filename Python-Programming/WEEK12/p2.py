#Birthday paradox#


import random
# create one empty list
l=[]
for i in range(30):
    l.append(random.randint(1, 365))
    # append random numbers between 1 to 365
    #append 30 of them
l.sort
print(l)

while(i<=len(l)-1):
    if (l[i]==l[i+1]):
        print("Report")
    else:
        print("Doesn't report")


