class Time:
    #definition operator overloading :-it means the behaviour of the operator behaves differently
      def __init__(self,hour=0,minute=0,second=0):
          self.hour=hour
          self.minute=minute
          self.second=second

      def __str__(self):
          return ('%.2d:%.2d:%2d' %(self.hour,self.minute,self.second))

      def __add__(self,other):
          x =self.hour+other.hour
          y=self.minute+other.minute
          z=self.second+other.second
          return x,y,z
time =Time()
start =Time(9,45,12)
duration =Time(13,12,10)
print(start+duration)