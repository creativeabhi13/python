# Loops in python

# Loops are used to repeat instructions

# while Loops
#syntax
# while condition:
#     # somework

count=1

# while count<5:
#     print("Hello ")
#     count +=1

# i=1
# while i<=100:
#     print("Jay Shree Sita Ram Jee")
#     i+=1
    
i=1
print("loop started")
while i<=10:
    print(i)
    i+=1
print("loop ended")

i=10
print("loop started")
while i>=1:
    print(i)
    i-=1
print(i)
print("loop ended ")




        
# Break and Continue
# Break:it is used to terminate the loop when encountered 
# Continue:it terminated the execution in the current iteration & continue execution of the loop with next iteration

# break example
# i=1 
# while i<=5:
#     print(i) # 1 2 3  
#     if(i==3):
#         break
#     i +=1
# print(i) # 3
# print("loop ended ") 
 


#continue example

i=0 
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i) # 0 1 2  4 5
    i +=1

print("loop ended ") 


