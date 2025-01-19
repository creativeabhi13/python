# function practise questions 

#1. Write a Function to print the length of a list. ( list is the parameter)

cities=["Delhi","Bengaluru","Kolkata","Mumbai","Hyderabad","Noida","Pune"]
car=["BMW","Jaguar","Alto","i10","Punch","Safari",]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(car)

#2. Write a Function to print the elements of a list in a single line. ( list is the parameter)

def print_el(list):
    for i in list:
        print(i, end=" ")
    print()

print_el(cities)
print_el(car)



#3. Write a Function  to find the factorial of n. (n is the parameter)

def factotial(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    print(fact)
factotial(5)



#4. Write a Function to convert USD to INR.

def converter(usd_val):
    inr_val=usd_val*86.58
    print(usd_val,"USD =", inr_val, "INR" )
converter(2000)

# 5. write a function which written "ODD" if it is a odd number else "EVEN"

def even_odd(num):
    if(num%2==0):
        print("EVEN")
    else:
        print("ODD")
    
even_odd(6)

# Recursion in Python

#6.Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if n==0:
        return 0
    return n+ sum(n-1)
print(sum(5))

# 7. Write a recursive function to print all elements in a list. Hint : use a list & index as parameters.

def print_list(list,idx=0):
    if(idx==len(list)):
        return 
    print(list[idx])
    print_list(list,idx+1)
    
fruits=["Apple","Banana","Mango","Orange","Grapes"]
print_list(fruits)