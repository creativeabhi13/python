def ProductArray(arr):
    result=1
    for x in arr:
        result*=x
    return result
list1=[1,2,3]
list2=[2,3,5,6,7]
print(ProductArray(list1))
print(ProductArray(list2))

    