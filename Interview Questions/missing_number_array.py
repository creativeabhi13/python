# Find missing number in an array  (using summation and XOR operations)

def missing_number():
    arr=[]
    n=int(input("Enter the number of elements in the array:"))
    for i in range(n):
        arr.append(int(input("Enter the element: ")))
    print("Array: ", arr)
    n=n+1
    total_sum=n*(n+1)//2
    sum_arr=sum(arr)
    missing_number=total_sum-sum_arr
    print("Missing number in the array is: ", missing_number)
missing_number()