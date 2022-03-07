#1. write a python program to find sum of n natural number
# num = int(input())
# if num < 0:
#     print("Enter a postiive a number")
#
# else:
#     sum = 0
#     while num > 0:
#         sum += num
#         num -= 1
#     print("The sum of n natural number is ", sum)

# 2.write python function to find factors of a number
# def printFactors(number):
#     print("The factors of",number,"are:-")
#     for count in range(1,number+1):
#         if number%count ==0:
#             print(count)
# number=int(input("Enter a number:-"))
# printFactors(number)

# 3.write a python program/function to find prime numnber
# def primeNumber(number):
#
#     for count in range(2,number):
#         if number%count==0:
#             print("the", number," is not prime Number:-")
#             break
#         else:
#             print("the", number," is a prime number")
#             break
#
# number=int(input("Enter a number:->"))
# primeNumber(number)

# 4.Write a python program to find a factorial/python of a number.
# def factorialOfaNumber(number):
#     factorial=1
#     if number<0:
#         print("Factorial cannot be of negative number")
#     elif number==0:
#         print("Factorial of 0 is 1")
#     else:
#         for count in range(1,number+1):
#             factorial=factorial*count
#         print("The Factorial of",number,"is",factorial)
# number=int(input("Enter a number:->"))
# factorialOfaNumber(number)

#5. Write a python program to find that the given year is leap year or not:
# year = int(input("Enter a year:->"))
# if year%4==0:
#      if year%100==0:
#          if year%400==0:
#              print(year,"is a leap year")
#          else:
#              print(year,"is not a leap year")
#      else:
#          print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")

# 6.write a program to Print star
# *
# * *
# * * *
# * * * *
# * * * * *
# def printStar(symbol):
#     for count in range(1,symbol+1): # 1 6
#         for recount in  range(1,count+1):#1 *
#             print("*",end=" ")
#         print("\n")
#
# symbol=int(input("Enter the number of star:->"))
# printStar(symbol)

# 7.write a program to Print star
# * * * * *
# * * * *
# * * *
# * *
# *
# def printStar(symbol):
# #     for count in range(1,symbol+1):
# #         for recount in  range(count,symbol+1):
# #             print("*",end=" ")
# #         print("\n")
# #
# # symbol=int(input("Enter the number of star:->"))
# # printStar(symbol)

# 8. Write a python program for swap of a two number
# a=int(input("enter a number:->"))
# b=int(input("enter a second number:->"))
# print("the number before swapping is",a,"amd",b)
# temp=a
# a=b
# b=temp
# print("the number after swap is",a,"and",b)

# 9. Write a python program to find quaratic eqaution roots
#
# import cmath
# a=int(input("enter the coefficient of a:->"))
# b=int(input("enter the coefficient of b:->"))
# c=int(input("enter the constant c:->"))
# d=b*2-4*a*c
# if d==0:
#     print("the roots are real and equal")
#     c1=-b/2*a
#     c2 = -b / 2 * a
# elif d>0:
#     print("the roots are real and distinct")
#     c1 = -b / 2 * a + cmath.sqrt(d) / 2 * a
#     c2 = -b / 2 * a - cmath.sqrt(d) / 2 * a
# else:
#     print("the roots are imaginary")
#     c1 = -b / 2 * a + cmath.sqrt(d) / 2 * a
#     c2 = -b / 2 * a - cmath.sqrt(d) / 2 * a
# print("the roots are c1=",c1,"and c2=",c2)

# 10. Write a python program to find lcm of two number
# number1=int(input("enter the first number:->"))
# number2=int(input("enter the second number:->"))
# if number1>number2:
#     lcm = number1
# else:
#     lcm=number2
# while True:
#     if lcm%number1==0 and lcm%number2==0:
#         print(lcm)
#         break
#     else:
#         lcm=lcm+1
# print("lcm of number is :->",lcm)

# 11.write a python program to find gcd/hcf of two number
# def hcfOFaNumber(number1,number2):
#     if number1>number2:
#         hcf=number1
#     else:
#         hcf=number2
#     while True:
#         if number1%hcf==0 and number2%hcf==0:
#             break
#         else:
#             hcf=hcf-1
#     print("hcf=",hcf)
#
#
# number1=int(input("Enter a number:->"))
# number2=int(input("enter a second number:->"))
# hcfOFaNumber(number1,number2)

# 12.Write a python program for factorial using recursion
# def factorialOfNumber(number):
#     if number==0:
#         return 1
#     elif number==1:
#         return 1
#     else:
#         return number*factorialOfNumber(number-1)
#
#
#
# number=int(input("Enter a number:->"))
# a=factorialOfNumber(number)
# print("the factorial of",number,"is:-",a)

# 13. write a python program for fabonacci series using recursion
# def fabonacci(number):
#     if number<=1:
#         return number
#     else:
#         return (fabonacci(number-1)+fabonacci(number-2))
#
# number=int(input("enter  a number:->"))
# print("the fabonacci series of ", number, "=")
# for num in range(number):
#    print("Number",fabonacci(num))
# 14.Write a python program to find the sum of n natural number by recursion
# def recursion_Sum(number):
#     if number<=1:
#         return number
#     else:
#         return number+recursion_Sum(number-1)
# number=int(input("Enter the number:->"))
# if number<0:
#     print("Enter a postive number")
# else:
#     print("the number is ",recursion_Sum(number))

# 15.Write a python program to construct floyd traingle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# row=int(input("enter the number of rows:->"))
# number=1
# print("The floyd's traingle is:-")
# for count in range(1,row+1):
#     for recount in range(1,count+1):
#         print(number,end="\t")
#         number+=1
#     print(" ")