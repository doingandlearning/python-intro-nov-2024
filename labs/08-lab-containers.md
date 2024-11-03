# Lab 8: Containers

In this lab, you will modify your number guess game to maintain a history of the guesses made by the user.

---

## Objective

Once the game is over, display a printout of the guesses made by the user in the order they were entered. This allows the user to review their gameplay.

---

## Implementation Details

- To maintain the guess history, use a **list**:
  - It should be modifiable.
  - It should allow duplicates (since the user may enter the same guess multiple times).
  - It should preserve the order of the guesses.

- Consider using a global variable to hold the list for simple access across functions.

---

## Sample Output

```
Welcome to the number guess game
Please guess a number between 1 and 10: 5
Sorry, wrong number
Your guess was lower than the number
Please guess again: 7
Sorry, wrong number
Your guess was lower than the number
Please guess again: 9
Sorry, wrong number
Your guess was lower than the number
Please guess again: 10
Well done, you won!
You took 4 attempts to complete the game
Your guesses were:
[5, 7, 9, 10]
Game Over
```

---

Incorporate this list of guesses into your existing game to track and display the guesses after the game concludes.
