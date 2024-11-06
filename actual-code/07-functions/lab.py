import random

target = random.randint(1,10)

def get_guess(prompt="What is your guess? "):
    result = "this is a string to trigger the while loop - it will be replaced by the user"
    while not result.isnumeric():
        result = input(prompt)
        if not result.isnumeric():
            print("Try again, that isn't an number")
    return int(result)

guess = None
guess_count = 0

while guess != target and guess_count < 4:
    guess = get_guess()
    guess_count += 1
    if guess == target:
        print(f"Well done! The answer was {guess}.")
    else:
        if guess < target:
            print("You were too low.")
        else:
            print("You were too high.")

print("Game over!")