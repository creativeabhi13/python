# Tuples in Python 
 # it is built-in data type that lets create immutable sequence of values.

tup=(87,64,33,95,76) #tup[0],tup[1]...

#tup[0]=85 # Not Allowed in python 

tup1=() # valid tuple but empty 

tup2=(1,) # tuple with value 1 with commas (comma is mandatory to create single tuple)

tup3=(1,2,3) # tuple with value 1,2,3

print(tup) # (87, 64, 33, 95, 76)
print(tup1) # ()
print(tup2) # (1,)
print(tup3) # (1, 2, 3)
print(type(tup)) # <class 'tuple'>

# these are not tuple we need to separate single element with comma separated value 
tup4=(1) # it will take 1 as integer
print(tup4) # 1
print(type(tup4)) #<class 'int'>

tup5=(1.0)
print(tup5) #1.0
print(type(tup5)) #<class 'float'>

tup6=("hello")
print(tup6) #hello
print(type(tup6)) #<class 'str'>


# Tuple Slicing 

print(tup[1:5]) # (64, 33, 95, 76)
print(tup[1:]) # (64, 33, 95, 76)

# Tuple Method

print(tup.index(87)) # return index of the first  occurance  => 0

tup=(1,2,4,5,1,6,7,1)
print(tup.count(1)) # return total occurance of  =>3

