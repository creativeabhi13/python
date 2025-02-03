# property decorator 
# @property decorator on any method in the class to use the method as a property.

# class Student:
#     def __init__(self):
#         pass
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         self.percentage=str((self.phy+self.chem+self.math)/3) + "%"

# student1=Student(89,98,98)
# print(student1.percentage) # 95

# student1.phy=86
# print(student1.phy) # 86
# print(student1.percentage) # still 95

#problem after changing the marks  so we can change tlike this 

class Student:
    def __init__(self):
        pass
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    
    # def calculatePercentage(self):
    #       self.percentage=str((self.phy+self.chem+self.math)/3) + "%"

    @property
    def percentage(self):
         return str((self.phy+self.chem+self.math)/3) + "%"

student1=Student(89,98,98)
print(student1.percentage)

student1.phy=86
print(student1.percentage)