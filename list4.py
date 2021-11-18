n=[-3,10,-5,5,20,16,-7,16,18,-20,339,929]
pos=0
neg=0
for i in range(len(n)):
    if n[i]>=0:
        pos+=1
    else:
        neg+=1
print(pos,neg)