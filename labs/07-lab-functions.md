# Lab 7: Number Guess Game

In this lab, you will create a simple number guessing game program, handling user input, using the `if` statement, and looping constructs. You should organize your code into functions.

---

## Game Logic

The basic flow of the game is:

1. The program randomly selects a number between 1 and 10.
2. It then asks the player to enter their guess.
3. It checks to see if the guess matches the randomly generated number:
   - If it does, the player wins.
   - If it doesn’t, it checks if the guess is higher or lower than the actual number and informs the player.
4. The player has 4 attempts to guess correctly; if they fail, they are informed that they lost and told the correct number.

---

## Sample Output

```
Welcome to the number guess game
Please guess a number between 1 and 10: 5
Sorry, wrong number
Your guess was higher than the number
Please guess again: 3
Sorry, wrong number
Your guess was lower than the number
Please guess again: 4
Well done, you won!
You took 3 attempts to complete the game
Game Over
```

---

## Hints

### Generate the Random Number

1. Use the `random` module to generate a random number.

   ```python
   import random
   number_to_guess = random.randint(1, 10)
   ```

   - This code generates a random integer between 1 and 10 (inclusive), which the player must guess.

### Obtain User Input

1. Get the player’s guess using the `input()` function and convert it to an integer.

   ```python
   guess = int(input('Please guess a number between 1 and 10: '))
   ```

   - This stores the guessed number in the variable `guess`.

---

## Define Functions

Think about what functions might be useful. You could create functions like:

- `print_welcome_message()`
- `get_user_guess()`
- `print_end_of_game_message()`

Keep it simple; you only need 2-4 functions for this game.

---

## Extension Points

If time allows, try adding additional features:

- **Cheat Mode**: If the user enters `-1`, display the number they need to guess and then continue the loop without counting this as an attempt.
