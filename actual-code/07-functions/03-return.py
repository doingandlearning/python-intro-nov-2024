def square(number):
    # number * number
    # number ** 2
    return number ** 2

print(square(3))

# user_name = input("Give me your name: ")
nine_squared = square(9)
print(nine_squared)

def get_a_number_from_the_user(prompt ="Give me a number: " ):
    result = "this is a string to trigger the while loop - it will be replaced by the user"
    while not result.isnumeric():
        result = input(prompt)
        if not result.isnumeric():
            print("Try again, that isn't an number")
    return int(result)

number1 = get_a_number_from_the_user()
number2 = get_a_number_from_the_user("Give me another number: ")
print(f"The sum of the numbers is {number1 + number2}")