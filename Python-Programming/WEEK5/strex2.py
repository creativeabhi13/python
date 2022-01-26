alpha="abcdefghijklmnopqrstuvwxyz"
ALPHA=alpha.upper()
a="abhishek"
# my expected output is bcijtif
c=''
#ceger cyfer key

i=0 
c=c+(alpha[(((alpha.index(a[i])+1)%26))])
c=c+(alpha[(((alpha.index(a[i+1])+1)%26))])
c=c+(alpha[(((alpha.index(a[i+2])+1)%26))])
c=c+(alpha[(((alpha.index(a[i+3])+1)%26))])
c=c+(alpha[(((alpha.index(a[i+4])+1)%26))])
c=c+(alpha[(((alpha.index(a[i+5])+1)%26))])
c=c+(alpha[(((alpha.index(a[i+6])+1)%26))])
print(c)

c="rishikesh"
#shift 1 sjtijlfti
#shift 2 tkujkmguj
b=" "
i=0 
k=2
b=b+(alpha[(((alpha.index(c[i])+k)%26))])
b=b+(alpha[(((alpha.index(c[i+1])+k)%26))])
b=b+(alpha[(((alpha.index(c[i+2])+k)%26))])
b=b+(alpha[(((alpha.index(c[i+3])+k)%26))])
b=b+(alpha[(((alpha.index(c[i+4])+k)%26))])
b=b+(alpha[(((alpha.index(c[i+5])+k)%26))])
b=b+(alpha[(((alpha.index(c[i+6])+k)%26))])
b=b+(alpha[(((alpha.index(c[i+7])+k)%26))])
print(b)
