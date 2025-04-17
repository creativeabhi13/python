# Find out pairs with given sum value of an array.

def target_pairs():
    arr=[]
    n=int(input("Enter the number of elements in the array:"))
    for i in range(n):
        arr.append(int(input("Enter the element: ")))
    print("Array: ", arr)
    target=int(input("Enter the target value: "))
    pairs=[]
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                pairs.append((arr[i],arr[j]))
    print("Pairs with target value are: ", pairs)

target_pairs()