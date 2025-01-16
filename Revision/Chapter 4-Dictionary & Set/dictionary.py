# Dictionary 
# Dictionaries are used to store data values in key:value pairs 

# they are unordered,mutable & don't allow duplicate keys

dict ={
    "name":"Abhishek",
    "cgpa":7.59,
    "grade":"C",
    "age":23
}

print(dict) # {'name': 'Abhishek', 'cgpa': 7.59, 'grade': 'C', 'age': 23}

print(type(dict)) # <class 'dict'>

print(dict['name']) # Abhishek

print(dict['age']) # 23

dict['cgpa']=8 

print(dict)  # {'name': 'Abhishek', 'cgpa': 8, 'grade': 'C', 'age': 23}

# key cannot be list other than that we can make use of any other data type as in python 

info={
    "name":"apnacollege",
    "subjects":["python","c++","java"],
    "topics":("dict","set"),
    "age":23,
    "is_adult":True,
    "marks":86.5
}

print(info)  # {'name': 'apnacollege', 'subjects': ['python', 'c++', 'java'], 'topics': ('dict', 'set'), 'age': 23, 'is_adult': True, 'marks': 86.5}

print(info['subjects']) # ['python', 'c++', 'java']

print(type(info)) # <class 'dict'>

print(type(info['subjects'])) # <class 'list'>


print(type(info['topics'])) # <class 'tuple'>

info['surname'] ="Kumar"

print(info)

# same key cannot be and it will override

#create empty string

str=""

# create empty list

list=[]

# create empty tuples
tup=()

# create empty dictionary 

dict1={}

print(str ,list,tup,dict1) #  [] () {}

print(type(str),type(list),type(tup),type(dict1)) # <class 'str'> <class 'list'> <class 'tuple'> <class 'dict'>