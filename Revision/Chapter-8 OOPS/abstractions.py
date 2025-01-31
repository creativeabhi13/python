# Data Abstraction :-Hiding the implementation details and showing only the functionality and essential details to the user.

class Car:
    def __init__(self):
        pass
    def __init__(self):
        self.accessalator=False
        self.brake=False
        self.clutch=False
    def start(self):
        self.accessalator=True
        self.brake=True
        self.clutch=True
        print("Car is Starting....")

car=Car()
car.start()