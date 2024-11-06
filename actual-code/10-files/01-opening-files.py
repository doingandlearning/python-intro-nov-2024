file = open("file1.txt", "r")

# Approach 1: Loop of the file
for line in file:
    if "1" in line:
        print(line)

# Approach 2: Get all of the text in a single string
# contents = file.read()  # gives me the whole file as one big blob of text
# print(contents[contents.find("2"):])

# Approach 3: Get the next line
# line1 = file.readline()
# print(line1)

# Approach 4: List of all the lines
# lines = file.readlines()
# print(lines)

file.close()
