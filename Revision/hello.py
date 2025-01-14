
# print a string /number 
print("Hello World")
print(23)

# variables
name="Abhishek Kumar"
age=23
price=25.99

print(type(name))
print(type(price))

print(name,age,price)


"""
Data Types 

Integers - whole number +ve ove 0
String- "Abhishek"
Float-3.5
Boolean-True or False
None-a=None

 """


# print sum
n1=7
n2=2
# print("The sum of" , n1 ,"and" , n2 ,"is : " ,n1+n2 )

# Arithmetic Operators 

sum = n1+n2

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2) 
print(n1%n2) # remainder =1
print(n1 ** n2) # n1^n2

# Comparision Operators / Relational Operators

# print(n1==n2) #False
# print(n1!=n2) #True
# print(n1>=n2) #True
# print(n1>n2) #True
# print(n1<=n2) #False
# print(n1<n2) #False

# Assignement Operators

# a=50 # Assignment Operator
# b=20
# num=10
# num1=5
# num +=num
# num1 *=num

# print(num,num1) # 20 100


# logical operator
#not
# print(not (a>b)) #False
# print(not (a<b)) # True

# #and
# print(a>b and a<b) #False
# print(a!=b and a>b) #Ture

#or

# print(a>b or a<b) #True
# print(a!=b or a>b) #True
# print(a<b or a>b ) #True


# Type Conversion -Converting one type of variable to another variable 
#type casting and type conversion
#type conversion done by interpreter automatically  whereas typecasting manually conversion

#type conversion -Automatic conversion


a = 2 #int
b = 4.5 #float
# float > int
sum =a+b # here integer will be automatically converted in float  # 2.0+4.5 =>6.5 

print(sum)

#type casting
a="2" # string
b=2 #int
# sum1 = a+b # it will fetch error we cannot add integer and string or string to float 
sum1 = int(a)+b #typecasting - convert a's value to ingeger
sum2 = a+str(b) #typecasting - conver b value to string
print(sum1) # 4
print(sum2) # 22
