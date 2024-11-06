import random

target = random.randint(1, 10)

def get_a_number_from_the_user(prompt="What is your guess? "):
    result = "this is a string to trigger the while loop - it will be replaced by the user"
    while not result.isnumeric():
        result = input(prompt)
        if not result.isnumeric():
            print("Try again, that isn't an number")
    return int(result)
print(target)

guess = None
guess_count = 0

while guess != target and guess_count < 4:
    guess = get_a_number_from_the_user()
    guess_count += 1
    if target == guess:
        print("Well done!")
    else:
        if guess < target:
            print(f"Your guess is too low, you have {4 - guess_count} guesses left.")
        else:
            print(f"Your guess is too high, you have {4 - guess_count} guesses left.")

print("Game over!")