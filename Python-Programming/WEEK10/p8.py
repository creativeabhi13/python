#find the lenght of the longest word from the set of the enetered word.
word=input("enter the word:-")
maxlen=0
while(word !="-1"):
    count=0
    for letter in word:
        count=count+1
    if count>maxlen:
        maxlen=count
    word=input("enter the word:-")
print("The length of the Longest word is %s:-" %maxlen)
