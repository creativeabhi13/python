#if statement 
print("please enter your date of birth")
birth_year=int(input())
current_year=2022
age=current_year-birth_year
if age<13:
    print("you are under age ! you cannot watch")
    print("wait until you are old enough to watch movie")
else:
    print("you are old enough you can watch this movie!, Enjoy")
    
print("have a nice time")
