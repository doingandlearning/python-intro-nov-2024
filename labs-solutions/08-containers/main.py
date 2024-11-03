import random

# Initialise the number to be guessed
number_to_guess = random.randint(1, 10)

# Initialise the number of tries the player has made
count_number_of_tries = 1

history = []

def print_welcome_message():
    print('Welcome to the number guess game')


def get_user_guess(prompt):
    return int(input(prompt))


def print_end_of_game_message():
    print('Game Over')


print_welcome_message()

# Obtain the users' guess
keep_playing = True
while keep_playing:

    # Obtain their next guess and increment number of attempts
    guess = get_user_guess('Please guess a number between 1 and 10: ')

    # Check to see they have not exceeded the maximum
    # number of attempts if so break out of loop otherwise
    # give the user come feedback
    if guess == -1:
        # Cheat mode
        print(f'Number to guess is {number_to_guess}')
    else:
        history.append(guess)

        if guess == number_to_guess:
            keep_playing = False
        elif guess < number_to_guess:
            print('Sorry wrong number')
            print('Your guess was lower than the number')
        else:
            print('Sorry wrong number')
            print('Your guess was higher than the number')

        count_number_of_tries += 1
        if count_number_of_tries > 4 and keep_playing:
            print('No guesses left')
            keep_playing = False

# Check to see if they did guess the correct number
if number_to_guess == guess:
    print('Well done you won!')
    print('You took', count_number_of_tries, 'goes to complete the game')
else:
    print("Sorry - you loose")
    print('The number you needed to guess was',
          number_to_guess)

print(f'Your guesses were: {history}')
print_end_of_game_message()
