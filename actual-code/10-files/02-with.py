# context manager
# file = open("file1.txt", "r")

with open("file1.txt", "r") as file:
    for line in file:
        print(line.strip())

# This is good practice because Python manages the closing of the file.