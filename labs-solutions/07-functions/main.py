import random

MAX_VALUE = 5
MIN_VALUE = 1

# Initialise the number to be guessed
number_to_guess = random.randint(MIN_VALUE, MAX_VALUE)

# Initialise the number of tries the player has made
count_number_of_tries = 1


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
    guess = get_user_guess(f'Please guess a number between {MIN_VALUE} and {MAX_VALUE}: ')

    # Check to see they have not exceeded the maximum
    # number of attempts if so break out of loop otherwise
    # give the user come feedback
    if guess == -1:
        # Cheat mode
        print(f'Number to guess is {number_to_guess}')
    else:
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

print_end_of_game_message()
