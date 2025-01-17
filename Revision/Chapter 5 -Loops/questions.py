# while loop practise questions

#1. Print numbers from 1 to 100

# num=1

# while num<=100:
#     print(num)
#     num +=1

#2. print numbers from 100 to 1

# num =100
# while num>=1:
#     print(num)
#     num -=1


#3. print multiplication table of a number 

# num=1
# mul=int(input("enter the table :"))
# while num<=10:
#     result=num*mul
#     print(num,"*",mul , "=" , result)
#     num +=1

# 4.Print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# idx=0
# nums=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# while idx<len(nums):
    
#     print(nums[idx]) 
    
#     idx +=1



#5. Search for a number x in this tuple using loop:[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# x=int(input("Enter the number you want to search in a tuple : "))
# nums=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# i=0

# while(i<len(nums)):
#     if(nums[i] == x):
#         print("found at idx",i)
#         break
#     else:
#         print("Finding......")
#     i +=1
  
# forloop

# 6.Print the elements of the following list using a loop:[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

list =[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for num in list:
    print(num)

# 7.Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

number=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x=int(input("Enter the number: "))
for num in number:
    if(num==x):
        print(x,"found")
        break
else:
    print("End")
    
# using for and range
#8.  print number from 1 to 100

# print("using For and Range")
# for i in range(1,101,1):
#     print(i)

#9. print number from 100 to 1

# print("using For and Range")
# for i in range(100,0,-1):
#     print(i)

#10. print multiplication table of a number n
num=int(input("Enter a number: "))
for i in range(1,11,1):
    result=num*i
    print(num,"X",i , "=" ,result)

#11.write a program to find sum of the first n numbers.(using while)
print("-------------Sum--------------")
sum=0
num=int(input("Enter a number : "))
i=1
while i<=num:
    sum =sum+i
    i +=1
   
print("sum using while ",sum)

# using for loop
sum=0
num=int(input("Enter a number : "))
for i in range(1,num+1,1):
    sum=sum+i
print("sum using for ", sum)
print("-------------Factorial--------------")
#12.write a program to find factorial of first n number (using for)
fact=1
num=int(input("Enter a number : "))
i=1
while i<=num:
    fact =fact*i
    i +=1
   
print("sum using while ",fact)

fact=1
num=int(input("Enter a number : "))
i=1
for i in range(1,num+1,1):
    fact =fact*i

   
print("sum using for ",fact)