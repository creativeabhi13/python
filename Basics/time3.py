class Time:
    #pure function
    def increment(time,seconds):
        time.second+=seconds

        if time.second >=60:
            time.second -=60
            time.minute+=1
        if time.minute >=60:
            time.minute -=60
            time.hour+=1
        return f'{time.hour}:{time.minute}:{time.second}'
t1=Time()
t1.hour =9
t1.minute=45
t1.second=40
print(Time.increment(t1,seconds=30))