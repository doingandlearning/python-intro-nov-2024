def print_message():
    """ A function the prints hello world """
    print("Hello, world!")

print("Hello, world!")
print_message()
print_message()
print_message()
print_message()

for i in range(100):
    print_message()



def print_my_message(message, person_speaking):   # arguments, parameters
    print("📣📣📣")
    print(f"{person_speaking} says `{message}`")
    print("📣📣📣")

print("Before the function")
print_my_message("I hope you had a yummy lunch", "Kevin")
print_my_message("I didn't get to go to R2 because I'm not on campus", "Kevin")
print_my_message("Instead I had a chicken and pesto wrap", "Kevin")

message = "I hope you had a yummy lunch"
person_speaking = "Kevin"
print("🎉🔉📣")
print(f"{person_speaking} says `{message}`")
print("🎉🔉📣")
message = "I didn't get to go to R2 because I'm not on campus"
person_speaking = "Kevin"
print("🎉🔉📣")
print(f"{person_speaking} says `{message}`")
print("🎉🔉📣")
message = "Instead I had a chicken and pesto wrap"
person_speaking = "Kevin"
print("🎉🔉📣")
print(f"{person_speaking} says `{message}`")
print("🎉🔉📣")




print("After the function")




