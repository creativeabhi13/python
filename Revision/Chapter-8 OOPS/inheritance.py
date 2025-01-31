#inheritance :-when one class(child/derived) derives the properties & methods of another class(parent/base) then it is called inheritance.

class Car:
    @staticmethod
    def start():
        print("Car Started....")
    
    @staticmethod
    def stop():
        print("Car Stopped....")

class BMW(Car):
    def __init__(self,name):
        self.name=name
        print("BMW Car Created Successfully!..")
car=BMW("BMW")