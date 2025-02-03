# Class Methods
# A class Method is bound to the class & receives the class as an implicit first argument.

# Note:-static Method can't acess or modify class state & generally for utility.


# class Person:
#     name="anomyous"

#     def __init__(self):
#         pass
#     def __init__(self,name):
#         self.name=name 
   
# p=Person("ABhishek") 
# print(p.name) #ABhishek
# print(Person.name) # anyomyous

# so the name is not changing to the class

# now we can change the class name via this also

 # we can modify this via this otherwise it will give error 

# class Person:
#     name="anomyous"
#     def changeName(self,name):
#        self.__class__.name=name
#     #    Person.name=name

# p=Person()
# p.changeName("Abhishek")
# print(p.name) # Abhishek 
# print(Person.name)  # Abhishek


# Now to avoid this we can use class method directly to the method and make it use
# in this scenraio directly change will happen at class
# class Person:
#     name="anomyous"
    
#     @classmethod
#     def changeName(cls,name): # cls will directly referring to the classs
#          cls.name=name

# p=Person()
# p.changeName("Abhishek")
# print(p.name) # Abhishek 
# print(Person.name)  # Abhishek


# Three types of methods 

# 1.static method => @staticmethod => it will not change bother attribute of classs or instance attributes ,
# 2.class method => @classmethod => class as a argument
# 3.Normal method => instance method  => self as an argument -object 