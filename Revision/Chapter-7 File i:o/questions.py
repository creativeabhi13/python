# Create a new file “test.txt” using python. Add the following data in it:
# with open("test.txt","w") as f:
#     f.write("Hello world from Abhishek Kumar\n We are learning File I/O \n")
#     f.write("using Java.\n I like Programming in Java. ")
# with open("test.txt","r") as f:
#     data = f.read()
#     print(data)


# with open("test.txt","w") as f:
#     f.write(new_data)

# WAF that replace all occurrences of “java” with “python” in above file.
# with open("test.txt","r") as f:
#     data=f.read()
# new_data=data.replace("Java","Python")
# print(new_data)


# Search if the word “learning” exists in the file or not.
def check_for_word():
    word = input("Enter the word to search: ")
    with open("test.txt","r") as f:
        data=f.read()
        if (word in data):
            print(f"{word} is present in the file")
        else:
            print(f"{word} is not present in the file")
check_for_word()

def check_for_line():
    word = input("Enter the word to search: ")
    data = True
    line_no=1
    with open("test.txt","r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(f"{word} is present in line number {line_no}")
            line_no+=1
check_for_line()