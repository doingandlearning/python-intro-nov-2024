# Lab 5: Flow of Control

There are three different exercises in this lab. You can select which you are interested in or do all three.

---

## Step 1: Check if Input is Positive or Negative

The aim of this exercise is to write a small program to test if an integer is positive or negative.

Your program should:

1. Prompt the user to input a number (use the `input()` function). You can assume that the input will be some sort of number.

2. Convert the string into an integer using the `int()` function.

3. Check whether the integer is positive, negative, or zero.

   Sample outputs from several runs of the program are given below.

   **Run 1:**

   ```
   Please input a number: 5
   Number is positive
   ```

   **Run 2:**

   ```
   Please input a number: -1
   Number is negative
   ```

   **Run 3:**

   ```
   Please input a number: 0
   Number is Zero
   ```

---

## Step 2: Test if a Number is Odd or Even

This exercise requires you to write a program to take input from the user and determine if the number is odd or even. You can assume that the user will enter a valid integer.

1. To test if a number is even, use:

   ```python
   (num % 2) == 0
   ```

   This will return `True` if the number is even.

2. Print out a message to the user to let them know the result.

   Example outputs:

   ```
   Please input a number: 1
   The number is odd
   ```

   ```
   Please input a number: 2
   The number is even
   ```

---

## Step 3 (Optional): Kilometres to Miles Converter

In this exercise, you should return to the kilometres to miles converter from the previous lab and add additional validations.

1. Modify your program to verify that the user has entered a positive distance (i.e., they cannot enter a negative number).

2. Modify your program to verify that the input is a number. If it is not a number, do nothing; otherwise, convert the distance to miles.

   - To check if a string contains only digits, use the `isnumeric()` method. For example, `'42'.isnumeric()` returns `True` if the string only contains numbers. Note that this method only works for positive integers, which is sufficient for this example.

3. Sample outputs:

   **Valid Input:**

   ```
   Please input the distance in kilometres: 15
   You entered the distance 15 in kilometres
   The distance in miles is 9.321
   ```

   **Invalid Input:**

   ```
   Please input the distance in kilometres: aaaaa
   Not an integer number
   ```
