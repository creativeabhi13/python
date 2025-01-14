l=[(2,5),(1,2),(4,4),(2,3),(2,1)]
for i in l:
    for j in l[::-1]:
        if i[-1]<j[-1]:
            l[l.index(i)]=j
            l[l.index(j)]=i
print(l)
