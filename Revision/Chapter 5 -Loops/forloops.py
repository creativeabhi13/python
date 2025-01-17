# for loop in python
# for loops are used for sequential traversal .For traversing list,string,tuple etc..

# for Loops

# for el in list:
#     # some work


list=[1,2,3]
for i in list:
    print(i) # 1 2 3
print("-------")    

str="Abhishek"
for char in str:
    print(char) # A b h i s h e k


print("-------")
# for loop with else

# for el in list:
#     some work
# else:
#     work when loops end 

list=[1,2,3]
for i in list:
    print(i) # 1 2 3 
else:
    print("Loop ended") # Loop ended
print("-------")

str="Abhishek"
for char in str:
    if(char=="k"):
        print("found") # A b h i s h e found
        break
    print(char)
else:
    print("Loop End")


print("-------")

# range 
# Range Function returns a sequence of numbers ,starting from 0 by default ,and increments by 1(by default) , and steps before specified number.

# range(start?,stop,step?)

seq =range(5)
print(seq[0]) # 0
print(seq[1]) # 1
print(seq[2]) # 2
print(seq[3]) # 3

#
print("-------")
for i in seq:
    print(i) # 0 1 2 3 4

print("----For Range-----")
for el in range(5): #range(stop)
    print(el) # 0 1 2 3 4
print("--------")
for el in range(1,5): #range(start,stop)
    print(el) # 1 2 3 4
print("--------")
for el in range(1,5,2):#range(start,stop,step)
    print(el)
print("--------")
print("--------")
for el in range(0,5,1):#range(start,stop,step)
    print(el)
print("--------")
for el in range(1,5,1): #range(start,stop,step)
    print(el)
print("----Even----")
#even number
for i in range(2,100,2):
    print(i)

print("----Odd----")
#even number
for i in range(1,100,2):
    print(i)

# pass statement 
# pass is a null statement that does nothing. It is used as a placeholder for future code.
for i in range(5):
    pass
print("hi")