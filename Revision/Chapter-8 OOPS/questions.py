# create 
# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:

    def __init__(self):
        pass

    def __init__(self,fullname,marks1,marks2,marks3):
        self.name=fullname
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
        print("Adding a New Student in Databse!..")

    def display(self):
        print("Name of Student is:",self.name)
        print("Marks of Student is:",self.marks1)
        print("Marks of Student is:",self.marks2)
        print("Marks of Student is:",self.marks3)
    
    def average(self):
        avg=(self.marks1+self.marks2+self.marks3)/3
        print("Average of Student is:",avg)

s1=Student("Abhishek Kumar",90,95,100)
s1.display()
s1.average()
