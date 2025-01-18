# Functions in python
# it is a block of the statement which perform a specific task.

# def func_name(parameter1,parameter2 => function parameter ): # function definition 
    #some work
   # return val
# func_name(arg1,arg2,=>function argument ): #function call 

# to avoid redudancy or redudant code we can create function and call the function
# if we have to do same work multiple time we can create function to avoid redudancy 

# def sum(a,b): # function definition 

#     s=a+b

#     return s

# num1=int(input("Enter the first number: "))

# num2=int(input("Enter the second number: "))

# s=sum(num1,num2) # function call

# print(s)  # 11


# print hello

# def print_hello():
#     print("Hello")
# print_hello()
# print_hello()

# Average of 3 numbers
# def avg(a,b,c):
#     avg=(a+b+c)/3
#     return avg
# n1=int(input("Enter 1st number: "))
# n2=int(input("Enter 2nd number: "))
# n3=int(input("Enter 3rd number: "))

# a=avg(n1,n2,n3)

# print(a)


# types of function
# 1. Built in function
# 2. user defined function

#1. Built in function => print() , len() , type() , range()

print("Abhishek", end=" ")
print("Kumar")  

# Abhishek Kumar

print("Abhishek\nKumar")
#Abhishek
#Kumar

#2. User Defined function => user will create or write by programmer function 

# case 1 :if we create a funtion and pass a parameter then we should pass argument while calling .

def cal_product(a,b):
    mul=a*b
    return mul
m=cal_product(8,4)
print(m)

# case 2:if we create a function we can also pass default parameter and without argument also we can call it 
# default parameter : it will assign the default value of the parameter ,which is used when no argument is passed.
def cal_product(a=5,b=2):  #default parameter  
    mul=a*b
    return mul
m=cal_product(8,4) # passed argument
m1=cal_product()  # no argument
print(m,m1)

# case 3:if we create a function and we are giving only one default arguments then we can give but the value should be come last 
def cal_sum(a,b=2):
    sum=a+b
    return sum
s=cal_sum(1) # passed  single argument 
s1=cal_sum(5,3)
print(s,s1)

