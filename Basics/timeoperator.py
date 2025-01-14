class Time:
    # init method
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

time=Time(9,45)

print(time)
# __str method
class T:
    def __str__ (self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
t1=T(10,45)
print(t1)
