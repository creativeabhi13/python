# List in Python
# A built in data types that stores a set of values
#it can stores elements of different types (integers,float,string,etc.)

# marks=[87,76,56,98]

student=["Karan",85,"Delhi"]

s=student[0]="Arjun"

l=len(student) # 3

# print(s,l,student,marks) #Arjun 3 ['Arjun', 85, 'Delhi'] [87, 76, 56, 98]
print(type(student)) # <class 'list'>
# print(student[3]) # out of range

# Strings => immutable 
# Lists => mutable
#similar to string slicing possible here itself

# List Slicing

#list_name[starting_idx:ending_idx]

marks =[86,76.5,89.7,67.4,95,76.4]

m1=marks[1:4] 

m=marks[0:4]  # is same  marks[:4] 

print(m) #[86, 76.5, 89.7, 67.4]

m2=marks[3:5]  

print(m1) # [76.5, 89.7, 67.4]

print(m2) # [67.4, 95]

m3=marks[1:] # it is same as marks[1:len(marks)]

print(m3) # [76.5, 89.7, 67.4, 95, 76.4]

m4=marks[-3:-1]

print(m4) # [67.4, 95]

# List Methods

list =[2,1,3]

# Append

list.append(4) # add one element at the end  => [2,1,3,4]

print(list) #[2, 1, 3, 4]

# Sort
list.sort() #sorts the list in ascending order => [1,2,3,4]

print(list) #[1, 2, 3, 4]

list.sort(reverse=True) # sorts  the list in descending order => [4,3,2,1]

print(list) #[4, 3, 2, 1]

list =[2,1,3]

# Reverse
list.reverse() # reverse the original list  => [3, 1, 2]

print(list) #[3, 1, 2]
# list.insert(idx,el) 
# Insert
list.insert(1,5)

print(list) #[3, 5, 1, 2]

# Remove

list.remove(1) # it removes the first occurance of the element => 1 is in the idx so it will be removed 

print(list) # [3, 5, 2]

list.pop(0) # it removes the index value  => 3 is at 0 idx so it will be removed 

print(list) #[5,2]