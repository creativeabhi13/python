# writing to a file
f=open("demo.txt","w") # open file in write mode
f.write("Hello World") # write data to file

f.close() # close the file


# Appending to a file

f1=open("demo1.txt","a") # open file in append mode
f1.write("Hello World1") # write data to file in append mode
f1.close() # close the file


# Reading a file
f3=open("demo.txt","r") # open file in read mode
data=f3.read() # read the data from file

f3.close() # close the file
print(data) # print the data

f4=open("demo1.txt","r") # open file in read mode
data1=f4.read() # read the data from file
f4.close() # close the file

print(data1) # print the data

