# Lists - mutable, ordered container

empty_list = []
print(empty_list)
print(type(empty_list))

beatle_list = ["John", "Paul", "George", "Ringo"]
print(len(beatle_list))
print(type(beatle_list[0]))
print(beatle_list[0:3])
print(beatle_list[::-1])

temperatures = [9, 12, 43.2, 12.3]
print(temperatures[0])
print(temperatures[1:])

print("Kevin" in beatle_list)

# name = input("What's your name? ")
# if name in beatle_list:
#     print("Hey, you're famous! Can we get a selfie?")

for name in beatle_list:
    print(f"{name} was a member of the Beatles")

beatle_list.append("Kevin")  # add a single item
print(beatle_list)

beatle_list.extend(["Maxime", "Pablo"])  # add a group of items
print(beatle_list)

beatle_list.remove("Kevin")
print(beatle_list)

del beatle_list[4:]
print(beatle_list)

beatle_list.sort()
print(beatle_list)

beatle_list.reverse()
print(beatle_list)

beatle_list_2 = beatle_list.copy()
beatle_list_2.append("Gert")
beatle_list.extend(["John", "John", "John"])
print(beatle_list_2)
print(beatle_list)

# print(beatle_list.index("John"))  # the first instance of our match
# print(beatle_list.pop(2))  # beatle_list[2]
#
# print(beatle_list.index("John"))  # the first instance of our match
# print(beatle_list.pop(3))  # beatle_list[2]
# print(beatle_list.index("John"))  # the first instance of our match
# print(beatle_list.pop(3))  # beatle_list[2]
# print(beatle_list.index("John"))  # the first instance of our match
# print(beatle_list.pop(3))  # beatle_list[2]

# if "John" in beatle_list:
#     print(beatle_list.index("John"))  # the first instance of our match
# else:
#     print("John not in list.")

while "John" in beatle_list:
    # index_of_john = beatle_list.index("John")
    # beatle_list.pop(index_of_john)
    beatle_list.pop(beatle_list.index("John"))

print(beatle_list)

# nesting

nested_list = [
    [0,1,2],
    [True, False],
    [(0,1), (2,3)]
]

print(nested_list[2][1][1])