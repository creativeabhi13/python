# strings
# string is a data type that stores a sequence of character .

# Basic Operations
# Concatenation
# "hello" + "world" =>"helloworld"
str="ABHISHEK"
#length of str
print(len(str))

#escape sequence character
str1="This is my Pen. My name is Abhishek Kumar."
print(str1)
str2="This is my Pen.\nMy name is Abhishek Kumar."
print(str2)
str3="This is my Pen.\tMy name is Abhishek Kumar."
print(str3)

#Indexing -it start with 0
str4="Abhishek_"
#     0123456789
# str4[0] is A 
# str4[1] is b
# ...........
# str4[9] is _
# str4[0] = B not possible (immutable)

#slicing 
print(str4[1:4]) #bhi
print(str4[:4]) #Abhi
print(str4[1:]) #bhishek

#-ve index backward counting
print(str4[-3:-1]) #ek

# String Functions
str5="i am a coder."

print(str5.endswith("er.")) # return  true if it ends with substr // True

print(str5.capitalize()) #capitalize the first char // I am a coder.

print(str5.replace("cod", "gam")) #replace all occurance of cod with gam // i am a gamer.

print(str5.find('a')) #return first index of 1st occurance.add()

print(str5.count('am')) # count the occurance of substring or a word

