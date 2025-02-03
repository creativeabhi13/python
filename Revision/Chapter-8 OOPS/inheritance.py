#inheritance :-when one class(child/derived) derives the properties & methods of another class(parent/base) then it is called inheritance.
#1. single inheritance
# class Car:
#     color="black"
#     @staticmethod
#     def start():
#         print("Car Started....")
    
#     @staticmethod
#     def stop():
#         print("Car Stopped....")

# class BMW(Car):
#     def __init__(self,name):
#         self.name=name
#         print("BMW Car Created Successfully!..")
# car=BMW("BMW")
# print(car.start())
# print(car.color)
# print(car.stop())

# Types of inheritance
# 1. Single Inheritance => Single Inheritance is a type of inheritance where a class inherits from only one class.
# base class => parent class 



# 2. Multiple Inheritance => Multiple Inheritance is a type of inheritance where a class inherits from more than one class.


# 3. Multilevel Inheritance => Multilevel Inheritance is a type of inheritance where a class inherits from a class, which 
# in turn inherits from another class.

#2. Multi Level Inheritance

# class Car:
#     color="black"
#     @staticmethod
#     def start():
#         print("Car Started....")
    
#     @staticmethod
#     def stop():
#         print("Car Stopped....")

# class Toyota(Car):
#     def __init__(self,brand):
#         self.brand=brand
#         print("Toyota Car Created Successfully!..")

# class Fortuner(Toyota):
#     def __init__(self,type):
#         self.type=type
#         print("Fortuner Car Created Successfully!..")

# car1=Fortuner("diesel")
# car1.start()

#3. Multiple Inheritance

# class A:
#     varA="Welcome to class A"
#     def methodA(self):
#         print("Method A is called")
# class B:
#     varB="Welcome to class B"
#     def methodB(self):
#         print("Method B is called")
# class C(A,B):
#     varC="Welcome to class C"
#     def methodC(self):
#         print("Method C is called")
# obj=C()
# obj.methodA()
# obj.methodB()
# obj.methodC()

# super method :=>
# super() method is used to call the parent class methods from the child class.
# super method is used to access the methods of the parent class from the child class.

class Car:
    def __init__(self):
        pass

    def __init__(self,type):
        self.type=type
    
    @staticmethod
    def Start():
        print("Car Started....")

    @staticmethod
    def Stop():
        print("Car Stopped....")
class Toyota(Car):
    def __init__(self):
        pass
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().Start()
        
        

car1=Toyota("Toyota","Electric")
print(car1.type)
