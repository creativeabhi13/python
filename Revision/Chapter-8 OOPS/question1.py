# let's Practise 
# Q1.Define a circle class to create a circle with radius r using the constructor.Define an Area() Method of class which the calculates the area of circle.add()
# Define the perimeter() method of a class which allow you to calculate the perimeter of a cirle.

class Circle:
    def __init__(self):
        pass
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7)* self.radius

r=int(input("Enter your radius : "))
c=Circle(r)
A=c.area()
P=c.perimeter()
print("Area : ",A,"\n","Perimter :",P)


# Q2. Define an Employee class with attributes like role,department, and salary.  This class also has showDetails()method.Create an Engineer Class
# that inherits properties from the employee & has additional attributes :name & age

class Employee:
    def __init__(self):
        pass
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def showDetails(self):
        print("Role: ",self.role)
        print("Dept: ",self.dept)
        print("salary: ",self.salary)

class Engineer(Employee):
    def __init__(self):
        pass
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75, 000")
    



e1 = Employee("accountant","Finance","60,000")
e1.showDetails()
print("-----")

eng1=Engineer("Abhishek Kumar",24)
eng1.showDetails()


# Q3. Create a class called order Which stores items & its price. Use Dunder function __gt__()  to convey that  order1>order 2 if price of order 1>price of order2 

class Order:
    def __init__(self):
        pass
    def __init__(self,item,price):
        self.item=item
        self.price=price
 
    def __gt__(self,odr2): # dundun function for greater than 
        return self.price>odr2.price

order1=Order("Chips",20)
order2=Order("Tea",15)

print(order1>order2) # True