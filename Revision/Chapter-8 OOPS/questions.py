# create 
# Q1. Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

# class Student:

#     def __init__(self):
#         pass

#     def __init__(self,fullname,marks1,marks2,marks3):
#         self.name=fullname
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3
#         print("Adding a New Student in Databse!..")

#     def display(self):
#         print("Name of Student is:",self.name)
#         print("Marks of Student is:",self.marks1)
#         print("Marks of Student is:",self.marks2)
#         print("Marks of Student is:",self.marks3)
    
#     def average(self):
#         avg=(self.marks1+self.marks2+self.marks3)/3
#         print("Average of Student is:",avg)

# s1=Student("Abhishek Kumar",90,95,100)
# s1.display()
# s1.average()

# Static Methods 
# Methods that don't use the self parameter (work at class level)

# class Student:
#    # @staticmethod # Decorator => Decorators allows us to wrap another function in order to extend the behavior of the wrapped function,
#    #  without permanently modifying it.
#     def college():
#         print("ABC college of Engineering")
# s2=Student()


# Q2. Create Account class with 2 Arguments -balance & account_number. Create a methods for debit,credit & check_balance.

class Account:
    #Default constructors
    def __init__(self):
        pass
    #Parametrized constructor
    def __init__(self,balance,account_number):
        self.balance=balance
        self.account_number=account_number
        print("Account Created Successfully!..")
    # Method to debit the amount
    def debit(self,amount):
        self.balance-=amount
        print("Rs.", amount," Debited Successfully!..")
        print("Total Balance is:",self.check_balance())
    # Method to credit the amount
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"Credited Successfully!..")
        print("Total Balance is:",self.check_balance())
    # Method to check the balance
    def check_balance(self):
        return self.balance

acc1=Account(10000,123456789)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(30000)
acc1.debit(9500)
