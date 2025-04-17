# write a python program to convert two list into a dicitionary 

# def list_to_dict():
#     keys=[1,2,3]
#     values=["one","two","three"]
#     result=dict(zip(keys,values))
#     print(result)

# list_to_dict()

# take user input 

def list_dict():
    keys=[]
    values=[]
    n=int(input("Enter the number of elements for dictionary:"))
    for i in range(n):
        keys.append(int(input("Enter the key: ")))
        values.append(input("Enter the value: "))
    result=dict(zip(keys,values))

    print(result)
list_dict()

def dict_to_tuple():
    d={}
    n=int(input("Enter the number of elements for dictionary:"))
    for i in range(n):
        key=input("Enter the key: ")
        value=input("Enter the value: ")
        d[key]=value
    result=tuple(d.items())
    print(result)
dict_to_tuple()
 

    