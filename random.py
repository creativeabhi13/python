n=[x//2 for x in range(20)]
print(n)

Python
3.9
.7(tags / v3
.9
.7: 1016
ef3, Aug
30
2021, 20: 19:38) [MSC v.1929 64 bit(AMD64)]
on
win32
Type
"help", "copyright", "credits" or "license()"
for more information.
    >> > my_string = "{},is a {} {} Engineering portal for {}"
>> > print(my_string.format("JIT", "COMPUTER", "SCIENCE"))
Traceback(most
recent
call
last):
File
"<pyshell#1>", line
1, in < module >
print(my_string.format("JIT", "COMPUTER", "SCIENCE"))
IndexError: Replacement
index
3
out
of
range
for positional args tuple
>> > 2 ** (3 ** 2)
512
>> > (2 ** 3) ** 2
64
>> > 2 ** 3 ** 2
512
>> >

def functional();


SyntaxError: invalid
syntax
>> >

def functional(): pr

>> > l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>> >
KeyboardInterrupt
>> > l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>> > [[row[i] for row in l] for i in range(3)]
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
>> > A = [[1, 2, 3, ], [4, 5, 6], [7, 8, 9]]
>> > [[col + 10 for col in row] for row in A]
[[11, 12, 13], [14, 15, 16], [17, 18, 19]]
>> > l = [[1, 2, 3], [4, 5, 6]]
>> > for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j] += 10
        l

SyntaxError: unexpected
indent
>> > l = [[1, 2, 3], [4, 5, 6]]
>> > for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j] += 10
        l

[[11, 2, 3], [4, 5, 6]]
[[11, 12, 3], [4, 5, 6]]
[[11, 12, 13], [4, 5, 6]]
[[11, 12, 13], [14, 5, 6]]
[[11, 12, 13], [14, 15, 6]]
[[11, 12, 13], [14, 15, 16]]
>> >

def foo(x):
    if (x == 1):
        return 1
    else:
        return x + foo(x - 1)


print(foo(4))

SyntaxError: unindent
does
not match
any
outer
indentation
level
>> >

def foo(x):
    if (x == 1):
        return 1
    else:
        return x + foo(x - 1)


print(foo(4))

SyntaxError: unindent
does
not match
any
outer
indentation
level
>> > A = "PYTHON"
A[0] = M
list(A)
>> > A = "PYTHON"
A[0] = M
list(A)

>> > A = ['P', 'y', 't', 'h', 'o', 'n']
print(A[:-4])
>> > A = ['P', 'y', 't', 'h', 'o', 'n']
print(A[:-4])

>> > n = [x // 2 for x in range(20)]
print(n)
SyntaxError: multiple
statements
found
while compiling a single statement
>> > n = [x // 2 for x in range(20)]
print(n)

SyntaxError: multiple
statements
found
while compiling a single statement
>> > n = [x // 2 for x in range(20)]
print(n)

SyntaxError: multiple
statements
found
while compiling a single statement
>> >