class Student:
    def __init__(self):
        pass

    def __init__(self,name):
        self.name=name
s1=Student("Shradha")
print(s1.name)
del s1.name
print(s1.name)