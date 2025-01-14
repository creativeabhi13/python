class Time:
    #Representation the time of day. attribures:hour,minute,and sconde
    def print_time(time):
        return '%.2d:%.2d:%.2d' %(time.hour,time.minute,time.second)
time=Time()
time.hour=11
time.minute=59
time.second=50
print(Time.print_time(time))