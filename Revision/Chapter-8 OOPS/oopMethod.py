# Methods 
# Methods are function that are defined inside a class.

# Creating Class 

class Student:
    # default constructor
    def __init__(self):
        pass
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("Adding a New Student in Databse!..")
    # Method to display the details of Student
    def display(self):
        print("Name of Student is:",self.name)
        print("Marks of Student is:",self.marks)

# Creating Object of class

s1=Student("Abhishek Kumar",90)
s1.display() # Name of Student is: Abhishek Kumar
             # Marks of Student is: 90
s2=Student("Aditya Krishnan",96)
s2.display() # Name of Student is: Aditya Krishnan
             # Marks of Student is: 96
