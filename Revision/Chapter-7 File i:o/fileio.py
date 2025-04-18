# File I/O in python

# python can be used to perform operations in files.(read, write, append, etc)

# Types of files:

# 1. Text files : .txt, .c, .py, .html, .docx, etc

# 2. Binary files : .jpg, .mp3, .mp4, .pdf, etc

# open ,read & Close file

# f=open("file_name","mode") # open file in read mode

# file_name : name of the file
# mode : mode in which file is to be opened


# f=open("file_name","r") # open file in read mode
# f=open("file_name","w") # open file in write mode
# f=open("file_name","a") # open file in append mode
# f=open("file_name","r+") # open file in read & write mode
# f=open("file_name","w+") # open file in write & read mode
# f=open("file_name","a+") # open file in append & read mode



# data =f.read() # read the data from file

# f.close() # close the file

# f=open("demo.txt","r") # open file in read mode

# data =f.read() # read the data from file

# print(data) # print the data

# print(type(data)) # print the type of data



# character     Meaning
# r             open file in read mode(default)
# w             open file in write mode
# a             open file in append mode
# x            create new file & open it for writing
# b           open file in binary mode
# t           open file in text mode(default)
# +          open file in read & write mode

# Reading a file

# data2=f.readline() # reads one line at a time

# print(data2)
# f.close() # close the file

# f= open("demo.txt","a+")
# # f.write("abc")
# print(f.read())
# f.write("abc")
# f.close() # close the file


# truncate - to remove the content of the file

# No Truncate - to keep the content of the file

# r+ read + overwrite (ptr start) - no truncate 

# w+ read + write overwrite (ptr start) - truncate

# a+ read + append (ptr end) - no truncate


# with syntax 
# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("Hello World")

# deleting the file :
# using the os module


import os
os.remove("test.txt")
# Module (like a code library) is a file written by another programmer that generally has
# a functions we can use.

