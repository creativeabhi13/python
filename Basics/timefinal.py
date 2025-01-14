class Time:
    def print_time(self):
        return '%.2d:%.2d:%.2d' %(self.hour,self.minute,self.second)

    def time_to_int(self):
        minutes=self.hour *60+self.minute
        seconds =minutes*60+self.second
        return seconds

    def int_to_time(self,seconds):

        minutes,self.second=divmod(seconds,60)
        self.hour,self.minute=divmod(minutes,60)
        return self

    def add_time(t1,t2):
        seconds=Time.time_to_int(t1)+Time.time_to_int(t2)
        return t1.int_to_time(seconds)
start=Time()
start.hour=9
start.minute=45
start.second=00
duration = Time()
duration.hour =1
duration.minute =35
duration.second =00

print(Time.print_time(start))
print(duration.print_time())
total=start.add_time(duration)

print(Time.print_time(total))
