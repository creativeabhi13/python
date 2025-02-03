#Polymorphism=> The ability to behave diffrently according to use case 
# => Many form to do same task with diffrently called polymorphism

#implicit overloading

# overriding 
# print(1+2) # 3
# print("abhi"+"shek") # abhishek # concatenate
# print([1,2,3]+[5,6,7]) # merge

#Complex Number

class Complex:
    def __init__(self):
        pass
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    # addition of a complex number    
    def __add__(self,num2): # dun dunder function to add real number 
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    
    # subtraction of a complex number 
    def __sub__(self,num2): # dun dunder function to sub real number 
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)
    

num1=Complex(1,3)
num1.showNumber()

num2=Complex(2,5)
num2.showNumber()

num3=num1+num2
num3.showNumber()

num4=num1-num2
num4.showNumber()


# operators & Dunder function 
# a + b # addition => a.__add__(b)
# a - b # subtraction => a.__sub__(b)
# a * b # multiplication => a.__mul__(b)
# a / b # division => a.__div__(b)
# a % b # modulous => a.__mod__(b)