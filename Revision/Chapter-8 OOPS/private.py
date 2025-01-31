#Private(like) attributes & methods
#Conceputal Implementation In Python
# Privates attributes & methods are meant to be used only within the class and are not accessible from outside the class
# Oops -> Public , Private 

# class Account:
#     def __init__(self):
#         pass
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass
#     # To make it private we use __ before the attribute name
#     # Private attribute
#     def reset_pass(self,new_pass):
#         self.__acc_pass=new_pass
#         print("Password Reset Successfully!..",self.__acc_pass)

# acc1=Account(123456789,"Abhishek@123")
# print(acc1.acc_no)
# acc1.reset_pass("Abhishek@1234")


# To make private attribute or method we use __ before the attribute or method name.
# Private attributes & methods are meant to be used only within the class and are not

# accessible from outside the class.
# Private attributes & methods are used to protect the data from the outside world.

# example for private attribute & method
class Account:
    def __init__(self):
        pass
    def __init__(self,id,pwd):
        self.id=id
        self.__pwd=pwd
    def __reset_pwd(self,new_pwd):
        self.__pwd=new_pwd
        print("Password Reset Successfully!..",self.__pwd)
    def display(self):
        print("Account ID:",self.id)
        self.__reset_pwd(self.__pwd)

acc1=Account(123456789,"Abhishek@123")
acc1.display()

