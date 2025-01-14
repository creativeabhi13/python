class Time:

    # prototying
    def print_time(time):
        return '%.2d:%.2d:%.2d' %(time.hour,time.minute,time.second)
    def time_to_int(time):
        minutes=time.hour *60+time.minute
        seconds =minutes*60+time.second
        return seconds

    def int_to_time(seconds):
        time=Time()
        minutes,time.second=divmod(seconds,60)
        time.hour,time.minute=divmod(minutes,60)
        return time

    def add_time(t1,t2):
        seconds=Time.time_to_int(t1)+Time.time_to_int(t2)
        return Time.int_to_time(seconds)




start=Time()
start.hour=9
start.minute=45
start.second=00
duration = Time()
duration.hour =1
duration.minute =35
duration.second =00

total=Time.add_time(start,duration)
print(Time.print_time(total))

