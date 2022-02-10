# find the day wise total rainfall for the entered duration of time eg.week,month,etc

days=int(input("enter the number of days:-"))
for i in range(1,days+1):
  total=0
  rainfall=int(input("enter the rainfall:"))
  while(rainfall !=-1):
    total=total +rainfall
    rainfall=int(input("enter the rainfall:"))
  print("Total rainfall for day {0} is {1}".format(i,total))