# Conditional Statement

# if-elif-else(SYNTAX)
    
# if(condition):
#     Statement 1
# elif(condition):
#     Statement 2
# else :
#     Statement N

light=input("Enter your light color : ")

if(light == "red"):
   print("STOP!")
elif(light == "yellow"):
   print("Go slowly!")
elif(light=="green"):
   print("Go!")
else:
   print(" Restart the program. Choose Appropriate color !")

print("End of Code !")

# Grade Student Marks

marks=int(input("Enter your Marks : "))

if(marks>=90):
   print("Excellent")
   print("A")
elif(marks>=80 and marks <90):
   print("B")
   print("Very Good")
elif(marks>=70 and marks <80):
   print("C")
   print("Good")
elif(marks>=60 and marks <70):
    print("D")
    print("Pass First Devision")
elif(marks>=40 and marks <60):
     print("E")
     print("Pass Second Division")
else:
   print("F")
   print("Reattempt the test")
    