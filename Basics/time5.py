class Time:
    # method
    def print_time(time):
        return '%.2d:%.2d:%.2d' %(time.hour,time.minute,time.second)
start=Time()
start.hour=9
start.minute=10
start.second=5
print(Time.print_time(start))
print(start.print_time())