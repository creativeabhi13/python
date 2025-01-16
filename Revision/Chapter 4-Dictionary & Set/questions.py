# Dictionary & set
# 1.Store following word meanings in a python dictionary :
# table:"a piece of furniture","list of facts & figures",cat:"a small animal"

dict={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts & figure"]
    }

print(dict) #{'cat': 'a small animal', 'table': ['a piece of furniture', 'list of facts & figure']}

#2. You are given a list of subjects for students .Assume one classroom is required for 1 subject.How many classrooms are needed by all students.

# "python" ,"java","c++","python","javascript"
# "java","python","java","c++","c"

set={"python" ,"java","c++","python","javascript","java","python","java","c++","c"}

print(set) # {'c', 'c++', 'python', 'java', 'javascript'}

print(len(set)) # 5


#3.WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
marks={}

x=int(input("enter phy marks: "))
marks.update({"phy":x})

x=int(input("enter math : "))
marks.update({"maths":x})

x=int(input("enter chem: "))
marks.update({"chem":x})


print(marks) #{'phy': 98, 'maths': 89, 'chem': 80}

#4.Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)

val1={9,"9.0"} #{9, '9.0'}

print(val1)  
val={
    ("float",9.0),
    ("int",9)
}
print(val) # {('float', 9.0), ('int', 9)}
