class Time:

    # Represents the time of the day .
    # attributes :hour,minute,second
    #imrpoved the time function
    def print_time(time):
        return '%.2d:%.2d:%.2d' %(time.hour,time.minute,time.second)
    def add_time(t1, t2):
        sum=Time()
        sum.hour=t1.hour+t2.hour
        sum.minute=t1.minute+t2.minute
        sum.second=t1.second+t2.second
        if sum.second>=60:
            sum.scond-=60
            sum.minute+=1
        if sum.minute>=60:
           sum.minute-=60
           sum.hour+=1
        return sum
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
