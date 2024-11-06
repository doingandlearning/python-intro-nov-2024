import random



def get_a_number_from_the_user(prompt="What is your guess? "):
    result = "this is a string to trigger the while loop - it will be replaced by the user"
    while not result.isnumeric():
        result = input(prompt)
        if not result.isnumeric():
            print("Try again, that isn't an number")
    return int(result)

def play_game():
    target = random.randint(1, 10)
    guess = None
    guess_count = 0
    guess_history = []

    while guess != target and guess_count < 4:
        guess = get_a_number_from_the_user()
        if guess in guess_history:
            print("You have already guessed that.")
            continue

        guess_history.append(guess)
        guess_count += 1
        if target == guess:
            print("Well done!")
        else:
            if guess < target:
                print(f"Your guess is too low, you have {4 - guess_count} guesses left.")
            else:
                print(f"Your guess is too high, you have {4 - guess_count} guesses left.")

    print(f"Here are you guesses: {guess_history}")

def ask_player_to_play_again():
    result = input("Do you want to play again? (yes/no) ")

    if result.lower() == "yes":
        return True
    elif result.lower() == "no":
        return False
    else:
        print("You can only say yes or no.")
        return ask_player_to_play_again()


# Client code -> use code
play_game()
wants_to_play_again = ask_player_to_play_again()

while wants_to_play_again:
    play_game()
    wants_to_play_again = ask_player_to_play_again()


print("Game over!")