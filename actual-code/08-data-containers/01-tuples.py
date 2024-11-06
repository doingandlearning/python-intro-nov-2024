empty_tuple = ()  # this is a tuple! rounded brackets!
print(empty_tuple)
print(type(empty_tuple))

#          0  1  2  3  4  5  6
tuple_1 = (1, 1, 2, 3, 5, 8, 13)
print(tuple_1)
print(type(tuple_1))
print(tuple_1.count(0))
print(len(tuple_1))

print(f"The value in position 4 is {tuple_1[4]}.")
print(f"The values from position 1 to position 4 are {tuple_1[1:4]}.")
print(f"The value in the last position is {tuple_1[-1]}.")
print(f"Every second value is {tuple_1[2:5:2]}")   # [start:end:step]   [the_start:the_end:in_steps_of_one]

tuple_1 = (1, 1, 2, 3, 5, 8, 13)
print(13 in tuple_1)
print(11 in tuple_1)

# user_number = int(input("Give me a integer between 1 and 13 and I'll tell you if it's a Fibonacci number: "))
#
# if user_number in tuple_1:
#     print("That is a Fibonacci number")
# else:
#     print("That is not a Fibonacci number.")

for fib_number in tuple_1:  # iterable
    print(fib_number)

tuple1 = (2,3,5,7,11)
tuple2 = ("Pablo", "Gianluigi", "Gert")
tuple3 = (True, 14, "Python is strange sometimes")
tuple4 = (tuple1, (1,4,9,16,25))

print(tuple4[1][2])

