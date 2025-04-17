# write a python program to count the frequency of word appearing in a string.
def freq_words():
    str=input("enter the string: ")
    words=str.split()
    d={}
    for word in words:
        if word not in d.keys():
            d[word]=0
        d[word]+=1
    print(d)
freq_words()
