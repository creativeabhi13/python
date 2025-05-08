# store frequency in dictionary 
# method 1:
# create a list where you can take input from user for the list element and also the list lenght

# Method 1:
num=int(input("Enter the length of the list "))
n=num
elements=[]

# taking input for the list input
for i in range(n):
    elem=input(f"Enter element{i+1}: ")
    elements.append(elem)

# storing frequency in a dictionary 

freq_dict={}
for elem in elements:
    if elem in freq_dict:
        freq_dict[elem] +=1
    else :
        freq_dict[elem] = 1
# printing the freqeuncey dictionary

print("Frequency of elments: ",freq_dict)

# Method 2:
# using Hashing Table
# using Hashing Table

n1 = int(input("Enter the length of the list: "))
num1 = n1
elements = []

# Taking input for the list elements
for i in range(num1):
    elem = input(f"Enter element {i + 1}: ")
    elements.append(elem)

# Storing frequency using a Hashing Table (dictionary)
hash_map = {}
for elem in elements:
    hash_map[elem] = hash_map.get(elem, 0) + 1

# Printing the frequency dictionary
print("Frequency of elements:", hash_map)