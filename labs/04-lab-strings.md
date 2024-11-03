# Lab 4: Python Strings

We are going to try out some of the string-related operations.

---

## Step 1: Explore Replacing a String

1. Create a string with words separated by commas and replace the commas with spaces. For example, replace all the commas in `'John,Andrew,Smith,21,London,UK'` with spaces. Now print out the resulting string.

   ```python
   original_string = 'John,Andrew,Smith,21,London,UK'
   ```

2. Print out the original string and the new string. Sample output might look like:

   ```
   Original string = 'John,Andrew,Smith,21,London,UK'
   New string = 'John Andrew Smith 21 London UK'
   ```

---

## Step 2: Handle User Input

1. Modify your program to additionally ask the user for two strings, concatenate them together with a space between them, and store them in a new variable called `new_string`.

2. Print out the value of `new_string`.

   Example:

   ```
   Please input the first string: John
   Please input the second string: Hunt
   John Hunt
   ```

---

## Step 3: Explore String Operations

1. Print out how long the contents of `new_string` is.

2. Convert the contents of `new_string` to all uppercase.

3. Check if `new_string` contains the string "Albus" as a substring.

4. Check if `new_string` matches "Hello World".

5. Use a formatted string to print out a message containing the value of `new_string`.

   Example output:

   ```
   Length of new_string = 9
   Upper case = JOHN HUNT
   The position of the string "Albus" is: -1
   new_string == "Hello World": False
   The value of new_string is John Hunt
   ```

---

## Step 4: Convert the Following Values into Strings

1. Define the following variables:

   ```python
   flag = True
   count = 10
   temperature = 32.6
   ```

2. Print out each of the above values and their type.

3. Convert the values to strings and print the results, using the `type()` function to confirm the new types.

   Sample output:

   ```
   flag = 'True' with type <class 'bool'>
   count = '10' with type <class 'int'>
   temperature = '32.6' with type <class 'float'>
   -------------------------
   flag_string = 'True' with type <class 'str'>
   count_string = '10' with type <class 'str'>
   temp_string = '32.6' with type <class 'str'>
   ```

---

## Step 5 (Optional): Convert Kilometres to Miles

1. Write code to convert a distance in kilometres into miles.

2. Take input from the user for a distance in kilometres using the `input()` function.

3. Convert the input value from a string into an integer using the `int()` function.

4. Convert this value into miles by dividing the kilometres by 0.6214.

5. Print out a message telling the user what the kilometres are in miles.

   Example:

   ```
   Please input the distance in kilometres: 15
   The distance in miles is 9.321
   ```
