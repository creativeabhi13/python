# 1.write a python program to find  the largest number in the list.
# sum=[10,20,50,30,70,40]
# max=sum[0]
# for count in range(1,len(sum)):
#     if sum[count]>max:
#         max=sum[count]
# print(max)

#2. Write a python program to find the sum of all the number in the list.
# sum=[10,30,20,50,60]
# sum1=sum[0]
# for count in range(1,len(sum)):
#     sum1+=sum[count]
# print(sum1)

#3. Write a python program to count the list of number which is positive and negative in the given list.
# number=[1,-3,5,-6,7,-7,9,10,-122,-67,56,12]
# positive=0
# negative=0
# for count in range(1,len(number)):
#     if number[count]>0:
#         positive+=1
#     else:
#         negative+=1
# print("Positive Number:-",positive,"and Negative Number are",negative)
#

# 4.
# From given list
# • gadgets = [“Mobile”, “Laptop”, 100, “Camera”,
# 310.28, “Speakers”, 27.00, “Television”, 1000,
# “Laptop Case”, “Camera Lens”]
# Write a python function to:
# • a)create separate lists of strings and numbers.
# • b)Sort the strings list in ascending order
# • c)Sort the strings list in descending order
# • d)Sort the number list from lowest to highest
# • e)Sort the number list from highest to lowest
# def listOperation(gadgets):
#     number=[]
#     str=[]
#     for item in gadgets:
#         if type(item)==int or type(item)==float:
#             number.append(item)
#         else:
#             str.append(item)
#     print("Number=",number)  #a
#     print("String=",str)     #a
#     str.sort()
#     print(str)             #b
#     str.reverse()
#     print(str)             #c
#     number.sort
#     print(number)          #d
#     number.reverse()
#     print(number)         #e
# gadgets =["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000,"LaptopCase","CameraLens" ]
# listOperation(gadgets)

#5.Write  a python function to find gcd of two number using list
# def gcd(x,y):
#     num1=[]
#     num2=[]
#     for count in range (1,x+1):
#         if x%count==0:
#             num1.append(count)
#     for recount in range (1,y+1):
#         if y%recount==0:
#             num2.append(recount)
#     num3=[]
#     for count in num1:
#         if count in num2:
#             num3.append(count)
#     print(num1)
#     print(num2)
#     print(num3)
# x=int(input("enter the  First number:->"))
# y=int(input("enter the second number:->"))
# gcd(x,y)

#6. Write a python function to perform matrix addition
# def matrixAdd():
#     a=[[1,2,3],[4,5,6],[7,8,9]]
#     b=[[9,8,7],[6,5,4],[3,2,1]]
#     c=[[0,0,0],[0,0,0],[0,0,0]]
#     for i in range(len(a)):
#         for j in range(len(a[0])):
#             c[i][j]=a[i][j]+b[i][j]
#     print(c)
#     for i in c:
#         print(i)
#
# matrixAdd()

#7.write a python function to perform matrix multiplication
# def matrixMul():
#     a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     b=[[9,8,7],[6,5,4],[3,2,1]]
#     c=[[0,0,0],[0,0,0],[0,0,0]]
#     for i in range(len(a)):
#         for j in range(len(a[0])):
#             for k in range(len(b)):
#                 c[i][j]+=a[i][j]+b[k][j]
#     print(c)
#     for i in c:
#         print(i)
# matrixMul()

# 8. Write a Python function that takes two lists and returns True if they have at least one common member.
# def commonMember(a,b):
#     count=0
#     for i in a:
#         if i in b:
#             count=1
#     if count==1:
#         return True
#     else:
#         return False
#
#
# a=[1,2,4,5,6,7,8]
# b=[2,6,9]
# l=commonMember(a,b)
# print(l)

# 9. Define a Python function alternating(l) that returns True if the values in the input list alternately go up and down (in a strict manner).
#For instance:
# • alternating([]) True
# • alternating([1,3,2,3,1,5]) True
# • alternating([3,2,3,1,5]) True
# • alternating([3,2,2,1,5]) False
# • alternating([3,2,1,3,5]) False

# def updown(l):
#     if len(l)==0 or len(l)==1:
#         return True
#     else:
#         return

# 10. A list rotation consists of taking the first element and moving it to the end.
# rotatelist([1,2,3,4,5],1) [2, 3, 4, 5, 1]
# rotatelist([1,2,3,4,5],3) [4, 5, 1, 2, 3]
#  rotatelist([1,2,3,4,5],12) [3, 4, 5, 1, 2]
# def rotate(list1,k):
#     if k==0:
#         return list1
#     else:
#         for i in range(k):
#             temp=list1[0]
#             del list1[0]
#             list1.append(temp)
#             print(list1)
#     return list1
#
#
# list1=[1,2,3,4,5]
# rotate(list1,5)

# 11 write a python function fro prime partition .
# def primecheck(m):
#     c=0
#     for i in range(2,m):
#         if m%i==0:
#             c+=1
#
#     if c == 0:
#         return True
#     else:
#         return False
# def partition(m):
#     l=[1]
#     for i in range(2,m+1):
#         if primecheck(i):
#            l.append(i)
#
#
#     for i in l:
#         for j in l:
#             if i+j==m:
#                return True
#
#     return False
# print(partition(7))
# 11. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# def last(n):
#     return n[-1]
# def sort_List_last(tuples):
#     return sorted(tuples,key=last)
# print(sort_List_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# spam={1:"abhi","age":21}
# print(spam.keys())
# # 12. Write a python program to add key to a dictonary
# d={"name":"abhishek"}
# print(d)
# d.update({"Age":30})
# print(d)
# d.setdefault("Sex","Male")
# print(d)

# 13. Write a Python script to concatenate following dictionaries to create a new one.
#dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic1.update({dic2})
# dic2.update({dic3})
# print(dic2)

# 14.rainfall
# def rainaverage(l):
#     raindata = {}
#     outputlist = []
#     for c, r in l:
#         if c in raindata.keys():
#             raindata[c].append(r)
#         else:
#             raindata[c] = [r]
#     print(raindata)
#
#     for c in raindata:
#         average = sum(raindata[c]) / len(raindata[c])
#         outputlist.append((c, average))
#         outputlist.sort()
#
#     return (outputlist)
#
#
# print(rainaverage([(1, 2), (1, 3), (2, 3), (1, 1), (3, 8)]))
# print(rainaverage([('Bombay', 848), ('Madras', 103), ('Bombay', 923), ('Bangalore', 201), ('Madras', 128)]))
# WRITE   a program to add string from staring and ending by taking 2 digit

# def string(c):
#     if len(c)==1:
#         return c+'$'
#     elif len(c)==2:
#         return c+c
#     else:
#         a=c[:2]
#         b=c[-2:]
#         d=a+b
#         return d
# c="abhishek"
# print(string(c))

# join the  dictionary
# def join(list1,list2):
#     dict3={}
#     for i in list1:
#         for j in list2:
#             if list1.index(i)==list2.index(j):
#                 dict3[i]=j
#     return dict3
# list1=[1,2,3,5,6,7,8,9]
# list2=[1,3,5,10,11,12,6]
# l=join(list1,list2)
# print(l)
# dictionary remove key
# def remove(dic1,key):
#     dic1.pop(key)
#     return dic1
# dic1={1: 1, 2: 3, 3: 5, 5: 10, 6: 11, 7: 12, 8: 6}
# print(remove(dic1,6))


def concat(dic1,dic2):
    return dic1.update(dic2)
dic1={1: 1, 2: 3, 3: 5, 5: 10, 6: 11, 7: 12}
dic2={"name":"abhishek","age":21}
l=concat(dic1,dic2)
print(l)
