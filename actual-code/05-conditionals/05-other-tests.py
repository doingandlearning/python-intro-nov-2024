user_input = input("Give me just numbers please: ")

if user_input.isnumeric():
    print("Well done!")
else:
    print("Oops! You gave me something that wasn't a number")