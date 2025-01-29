# oop map is real world scenarios, we started using object in code.
# This is the object oriented programming.

# class is a blueprint for creating objects.

# Creating Class

# class Student:
#     name="Aditya Krishnan"
#     roll=101

# # Creating Object (instance) of class  => Object is an instance of class
# s1=Student()
# print(s1.name,s1.roll)
# print(s1)

# class Car:
#     color="blue"
#     brand="BMW"

# car1=Car()
# print(car1.color)
# print(car1.brand)

# Constructor
# __init__ Function
# All classes have a function called __init__(), which is always executed when the clas being initiated.

# creating Class 

# class Student:
#     name="Abhishek Kumar"
#     # def __init__(self,fullname):
#     #     self.name=fullname
#     def __init__(self):
#         print(self.name)
#         print("Adding a New Student in Database!..")

# # Creating Object of class
# s1=Student()




# The self is reference to the current instance of the class, and is used to access variables that belongs to the class.

# class Student:

#     #Default constructors 
#     def __init__(self):
#         pass
    
#     #Parametrized constructor
#     def __init__(self,fullname,marks):
#         self.name=fullname
#         self.marks=marks
    
#         print("Adding a New Student in Databse!..")
   

# # Creating Object of class
# s1=Student("Abhishek Kumar",90)
# print(s1.name,s1.marks) # Abhishek Kumar 90

# s2=Student("Aditya Krishnan",96)
# print(s2.name,s2.marks) # Aditya Krishnan 96


# Class & Instance Attributes # attributes meaning any variable or data
# class.attr , instance.attr

# class.attributes : - attributes that are defined in the class and are same for all instances of the class.

# instance.attributes : - attributes that are defined inside the constructor and are different for all instances of the class.

# Student -> S1 , S2 , S3 => name, roll, marks => class attributes  => school => instance attributes => marks ,name,  

# class Student -> name, roll => class attributes   

# instance attributes => marks => different for all instances of the class.

class Student:

    #Default constructors 
    def __init__(self):
        pass
    college_name="IIT Bombay"
    name="Abhishek" # class attribute 
    #Parametrized constructor
    def __init__(self,fullname,marks):
        self.name=fullname # instance attribute or object attribute
        self.marks=marks
    
        print("Adding a New Student in Databse!..")
   

# Creating Object of class
#if class attribut is there and also object attribute is there then object attribute will be given priority.
# object attr >> class attr
# class attr will be same for all instances of the class.
# instance attr will be different for all instances of the class.
s1=Student("Abhishek Kumar",90)
print(s1.name,"|",s1.marks,"|",s1.college_name) # Abhishek Kumar 90


s2=Student("Aditya Krishnan",96)
print(s2.name,"|",s2.marks,"|",s1.college_name) # Aditya Krishnan 96


