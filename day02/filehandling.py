# file handling
# open function
# opening
# reading
# writing

# open(<file name> <file location>, <mode>)

# close()
# with open()

file = open("something.txt", mode ="r")

data = file.readline()
print (data)

file.close()


with open("something.txt" , mode = "r") as file:
    data = file.readline()
    print(data)
    
try:
    with open("sample/newfile.txt", "a") as file:
        file.writelines(["\nThis is a new file created!", "\nAnother line to be added."])
except FileNotFoundError as e:
    print("Error: ", e)