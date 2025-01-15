# String Questions
#1. write a program to take input from a user first name and print its length.

# str=input("Enter your first name :") 
# print(str,len(str))

#2. write a program to find a occurance of $ in a string

# str=input("Enter your string with $ :") 
# print(str,str.count("$"))

#condtional 

# 3. Odd Even
#  
# num=int(input("Enter your number : "))

# if(num%2==0):
#     print("EVEN !")
# else:
#     print("ODD!")

#4. greatest of 3 number

# num1=int(input("Enter 1st num: "))

# num2=int(input("Enter 2nd num: "))

# num3=int(input("Enter 3rd num: "))

# if(num1>=num2 and num1>=num3):
#     print(num1 ,"is a Greatest!")

# elif(num2>=num1 and num2>=num3):
#     print(num2, "is a Greatet!")

# else:
#     print(num3, "is a Greatest!")

#5. mutliple of 7 or not

num=int(input("Enter your number:"))

if(num%7==0):
    print("it is a multiple of 7!")
else:
    print("it is not a multiple of 7!")
