'''List in python
ts are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set,
 rand Dictionary, all with different qualities and usage.

Lists are created using square brackets:
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.
list are mutable

Python has a set of built-in methods that you can use on lists.
Method 	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

l=[1,2,3,4,99,94,35,45,6]
print(l)
l.append(100)
print(l)
l.remove(6)
print(l)
x=l.copy()
print(x)
l.reverse()
print(l)
r=[11,22,33,44,55,66,77]
s=[]
s.append(l)
print(s)
s.append(r)
print(s)
t=[10,20,30,40,50]
r.append(t)
print(s)
print(s[0])
print(s[0][0])
print([s[1][1]])
