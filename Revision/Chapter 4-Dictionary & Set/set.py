# Set in Python

# set is a collection unordered items.

# Each element in the set must be unique and immutable

# sets is mutable

# sets -> element is immutable 

# list cannot be added because it is mutable 

nums = {1,2,3,4}

print(nums) # {1, 2, 3, 4}

print(type(nums)) # <class 'set'>

# empty sets



nums1 =set()

print(nums1) #  set()

print(type(nums1)) # <class 'set'>

# it will ignore duplicate value

collection={1,2,4,2,1,4,"hello","ram"}

print(collection) # {1, 2, 'ram', 4, 'hello'}

print(len(collection)) # 5 total numbers of items 

# Methods in Set

# set.add(el) # add element to the sets

# set.remove(el) # remove element from the sets

# set.clear() # empties the set 

# set.pop() # remove the random values 

collection1 = set()

collection1.add(5)

print(collection1) # {5}

collection1.add(6)

collection1.add(7)

print(collection1) # {5,6,7}

collection1.remove(5)


print(collection1) # {6,7}


collection1.add("red")

print(collection1) # {'red', 6, 7}

collection1.pop()

print(collection1) # {6, 7}

collection1.clear()

print(collection1) # set()


# union and intersection

# set.union(set2) #combines both set value and return new => total unique value will be return

# setx.intersection(set) # combines common value and return new


set={1,"ram",2,"shyam",3,"raju",6,7,8}

print(set) # {1, 2, 3, 6, 7, 8, 'ram', 'shyam', 'raju'}

set1={5,2,"kunal","sita","ram","radhe","shyam",1}

print(set1) # {1, 2, 'sita', 5, 'kunal', 'radhe', 'ram', 'shyam'}

u=set.union(set1)

i=set.intersection(set1)

print(u) # {1, 2, 3, 'sita', 5, 6, 7, 8, 'kunal', 'radhe', 'ram', 'raju', 'shyam'}

print(i) # {1, 2, 'shyam', 'ram'}






