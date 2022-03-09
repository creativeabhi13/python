#1
# class Time:
#    #Representation the time of day. attribures:hour,minute,and sconde
#    def print_time(time):
#        return '%.2d:%.2d:%.2d' %(time.hour,time.minute,time.second)
# time=Time()
# time.hour=11
# time.minute=59
# time.second=50
# print(Time.print_time(time))


#2
# class Time:
#     # represents the time of the day
#     # attributes :hour,minute,second
#     def print_time(time):
#         return "%.2d:%.2d:%.2d" %(time.hour,time.minute,time.second)
#
#     def add_time(t1,t2):
#         sum=Time()
#         sum.hour=t1.hour+t2.hour
#         sum.minute=t1.minute+t2.minute
#         sum.second=t1.second+t2.second
#         return sum
# start=Time()
# start.hour=9
# start.minute=45
# start.second=30
# stop=Time()
# stop.hour=1
# stop.minute=35
# stop.second=00
# total=Time.add_time(start,stop)
# print(Time.print_time(total))

# 3
# class Time:
#
#    # Represents the time of the day .
#    # attributes :hour,minute,second
#    #imrpoved the time function
#    def print_time(time):
#        return '%.2d:%.2d:%.2d' %(time.hour,time.minute,time.second)
#    def add_time(t1, t2):
#        sum=Time()
#        sum.hour=t1.hour+t2.hour
#        sum.minute=t1.minute+t2.minute
#        sum.second=t1.second+t2.second
#        if sum.second>=60:
#            sum.scond-=60
#            sum.minute+=1
#        if sum.minute>=60:
#           sum.minute-=60
#           sum.hour+=1
#        return sum
# start=Time()
# start.hour=9
# start.minute=45
# start.second=00
# duration = Time()
# duration.hour =1
# duration.minute =35
# duration.second =00
#
# total=Time.add_time(start,duration)
# print(Time.print_time(total))


# 4.modifiers
# class Time:
#    #pure function
#    def increment(time,seconds):
#        time.second+=seconds
#
#        if time.second >=60:
#            time.second -=60
#            time.minute+=1
#        if time.minute >=60:
#            time.minute -=60
#            time.hour+=1
#        return f'{time.hour}:{time.minute}:{time.second}'
# t1=Time()
# t1.hour =9
# t1.minute=45
# t1.second=40
# print(Time.increment(t1,seconds=30))

#5.prototyping
# class Time:
#
#    # prototying
#    def print_time(time):
#        return '%.2d:%.2d:%.2d' %(time.hour,time.minute,time.second)
#    def time_to_int(time):
#        minutes=time.hour *60+time.minute
#        seconds =minutes*60+time.second
#        return seconds
#
#    def int_to_time(seconds):
#        time=Time()
#        minutes,time.second=divmod(seconds,60)
#        time.hour,time.minute=divmod(minutes,60)
#        return time
#
#    def add_time(t1,t2):
#        seconds=Time.time_to_int(t1)+Time.time_to_int(t2)
#        return Time.int_to_time(seconds)
#
#
#
#
# start=Time()
# start.hour=9
# start.minute=45
# start.second=00
# duration = Time()
# duration.hour =1
# duration.minute =35
# duration.second =00
#
# total=Time.add_time(start,duration)
# print(Time.print_time(total))

# 6.Method:- a function inside the class and it always present inside the class
# class Time:
#    # method
#    def print_time(time):
#        return '%.2d:%.2d:%.2d' %(time.hour,time.minute,time.second)
# start=Time()
# start.hour=9
# start.minute=10
# start.second=5
# print(Time.print_time(start))
# print(start.print_time())

#7.using self method approach

# class Time:
#    def print_time(self):
#        return '%.2d:%.2d:%.2d' %(self.hour,self.minute,self.second)
#
#    def time_to_int(self):
#        minutes=self.hour *60+self.minute
#        seconds =minutes*60+self.second
#        return seconds
#
#    def int_to_time(self,seconds):
#
#        minutes,self.second=divmod(seconds,60)
#        self.hour,self.minute=divmod(minutes,60)
#        return self
#
#    def add_time(t1,t2):
#        seconds=Time.time_to_int(t1)+Time.time_to_int(t2)
#        return t1.int_to_time(seconds)
# start=Time()
# start.hour=9
# start.minute=45
# start.second=00
# duration = Time()
# duration.hour =1
# duration.minute =35
# duration.second =00
#
# print(Time.print_time(start))
# print(duration.print_time())
# total=start.add_time(duration)
#
# print(Time.print_time(total))


# 7.init method
# class Time:
#    # init method
#    def __str__(self):
#        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
#    def __init__(self,hour=0,minute=0,second=0):
#        self.hour = hour
#        self.minute = minute
#        self.second = second
# time=Time(9,45)
# print(time)
# # __str method
# class T:
#    def __str__ (self):
#        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
#    def __init__(self,hour=0,minute=0,second=0):
#        self.hour = hour
#        self.minute = minute
#        self.second = second
# t1=T(10,45)
# print(t1)

#.8operator overloading
# class Time:
#     def __str__(self):
#         return "%.2d:%.2d:%.2d" %(self.hour,self.minute,self.second)
#     def __init__(self,hour=0,minute=0,second=0):
#         self.hour=hour
#         self.minute=minute
#         self.second=second
#     def __add__(self,other):
#         x=self.hour+other.hour
#         y=self.minute+other.minute
#         z=self.second+other.second
#         return x,y,z
# time=Time()
# start=Time(9,45,12)
# stop=Time(13,12,10)
# print(start+stop)


# 9 polymorphism
# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] = d[c] + 1
#     return d
#
#
# t = ['spam', 'egg', 'spam', 'spam', 'bacon',
#      'spam']
#print(histogram(t))
class Card:
    suit_names = ["clubs", "diamond", "hearts", "spades"]
    rank_names = ["None", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])


c = Card(1, 12)
print(c)

King
of
diamond

12.)
Import
requests
r = requests.get(“https: // creativeabhi13.github.io”)
r.raise_for_status()
file = open(“hello.txt”, ”wb”)
For
i in r.iter_content(2000):
file.write(l)
file.close()

# The complete progress for downloading and saving a file.
#
# Call requests get() to download the file.
# Call open()with wb to create a new file in write binary mode.
# Loop over the purpose objects iter_content() method.
# Call write() on Each iteration to write content to the file.
# Call close() to close the file.

13.)
Import webbrowser, sys
% % file abhi.py
If len(sys.argv) > 1:
    r =” “.join(sys.argv[1:])
webbrowser.open(“https: // www.google.com / search?q =”+r)
% run
abhi.py
python

The
complete
progress
for downloading and saving a file.

1.)create a file, we will use % keyboard file to search create a file
2.)we will use the module webbrowser.sys
3.) if len(sys.srgv > 1
Then open the browser and open the website
4.) run the program




















14.) web scraping:-web
Scraping is a
method
which is used in a
program
to
download and process
content
from the web.

Web
browser: - it
will
just
open
the
file or it
helps
us
to
open
a
file.

Requests: - it
will
download
the
file and web pages
from the internet.

Beautiful
soup: - it
will
parse
html
file
extension and format
the
web
pages
which
are
written in it.

Selenium: -it
Launches and controls
a
web
browser.Selenium is able
to
fill in forms and simulate
mouse
clicks in this
browser.





