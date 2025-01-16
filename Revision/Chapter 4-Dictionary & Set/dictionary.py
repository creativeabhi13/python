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

lis=[]

# create empty tuples
tup=()

# create empty dictionary 

dict1={}

print(str ,lis,tup,dict1) #  [] () {}

print(type(str),type(lis),type(tup),type(dict1)) # <class 'str'> <class 'list'> <class 'tuple'> <class 'dict'>

# Nested Dictionaries

student={
    "name":"Abhishek Kumar",
    "score":{
        "chem":78,
        "maths":87,
        "phy":78
    },
}

print(student) # {'name': 'Abhishek Kumar', 'score': {'chem': 78, 'maths': 87, 'phy': 78}}

print(student['score']['maths']) # 87

print(student['score']['phy']) # 78

# Dictionaries Methods
print(student.keys()) #  dict_keys(['name', 'score'])

print(student.values()) # dict_values(['Abhishek Kumar', {'chem': 78, 'maths': 87, 'phy': 78}])


# myDict.keys() # return All keys
 
# myDict.values() # returns All Values

# myDict.items() # returns all (key,val) pairs as tuples

# myDict.get("key") # returns  all value according to values

# myDict.update(newDict) # returns the specific items to dictionaries

print(student.items()) # dict_items([('name', 'Abhishek Kumar'), ('score', {'chem': 78, 'maths': 87, 'phy': 78})])


print(list(student.items())) # [('name', 'Abhishek Kumar'), ('score', {'chem': 78, 'maths': 87, 'phy': 78})]

print(student.get('score')) # {'chem': 78, 'maths': 87, 'phy': 78}

print(student['score'])  # {'chem': 78, 'maths': 87, 'phy': 78}

print(student['score']['maths'])  # 87

student.update({"city":"delhi"})

print(student) # {'name': 'Abhishek Kumar', 'score': {'chem': 78, 'maths': 87, 'phy': 78}, 'city': 'delhi'}

new_dict={
    "state":"Delhi"
}

student.update(new_dict)

print(student) # {'name': 'Abhishek Kumar', 'score': {'chem': 78, 'maths': 87, 'phy': 78}, 'city': 'delhi', 'state': 'Delhi'}