
# List
#1. Write a Program to ask the user to enter name of their 3 favorite movies & store them in a list.
# create an Empty list 
movies=[]

# # asking user to enter the movie
# movie1=input("Enter your First movie : ")
# movie2=input("Enter your Second movie : ")
# movie3=input("Enter your Third movie : ")


# # Append the list
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

# # print movie
# print(movies)

movies.append(input("Enter your First Movies : "))
movies.append(input("Enter your Second Movies : "))
movies.append(input("Enter your Third Movies :  "))

print(movies)


#2. Write a Program to check if a list contains palindrome of elements # use copy Method

# Palindrome - 12321 or racecar from left to right or right to left it should be same


list=[1,2,3,2,]

list1=list.copy()

reverse=list1.reverse()

if(list == list1):
    print("Palindrome")
else:
    print("Not a Palindrome")

# Tuples

# 3. Write a Program to count the number of students with the "A" grade in the following tuple

grade=("C","D","A","A","B","B","A")
print(grade.count("A"))

# 4. stores the above value in list and sort them from "A" to "D"


grade1=["C","D","A","A","B","B","A"]
grade1.sort()
print(grade1)


