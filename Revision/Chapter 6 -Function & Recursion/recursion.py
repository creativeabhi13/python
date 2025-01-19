# Recursion in Python
# when a function call itself repeatedly.

# print n to 1 backwards
def show(n):
    if n == 0: # base case
        return
    print(n) # print n
    show(n-1) # call show() with n-1
  
show(5) # 5 4 3 2 1

# factoria of n
def fact(n):
    if( n==0 or n==1): # base case
        return 1
   
    return n * fact(n-1) # recursive call
f=fact(5) # 120
print(f) # 120

# Working of recursion via stack
# 1. fact(5) -> 5 * fact(4) -> 5 * 4 * fact(3) -> 5 * 4 * 3 * fact(2) -> 5 * 4 * 3 * 2 * fact(1) -> 5 * 4 * 3 * 2 * 1 * fact(0) -> 5 * 4 * 3 * 2 * 1 * 1
# 2. show(5) -> 5 -> show(4) -> 4 -> show(3) -> 3 -> show(2) -> 2 -> show(1) -> 1 -> show(0) -> 0

