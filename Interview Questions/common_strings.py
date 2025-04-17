# Write a Python Program to find out the common strings between two strings ?.remove duplicate words from a given string

def common_strings(str1, str2):
    str1=input("Enter the first string: ")
    str2=input("Enter the second string: ")
    print("String 1: ", str1)
    print("String 2: ", str2)   
    str1=set(str1)
    str2=set(str2)
    common=str1&str2
    print("Common strings between two strings are: ", common)

common_strings("abhishek", "rishikesh")